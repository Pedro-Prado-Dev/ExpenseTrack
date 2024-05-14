import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Gasto
from database import session

app = Flask(__name__)
CORS(app)  # Isso habilita o CORS para todos os endpoints da aplicação


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/gastos', methods=['POST'])
def adicionar_gasto():
    novo_gasto = request.json  # Obtém os dados do JSON enviado na requisição
    descricao = novo_gasto.get('descricao')
    valor = novo_gasto.get('valor')

    if not descricao or not valor:
        return jsonify({"error": "Descrição e valor são campos obrigatórios"}), 400

    try:
        # Cria um novo objeto Gasto com os dados fornecidos
        novo_gasto = Gasto(descricao=descricao, valor=valor)
        session.add(novo_gasto)
        session.commit()
        return jsonify({"message": "Gasto adicionado com sucesso", "gasto_id": novo_gasto.gasto_id}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/gastos', methods=['GET'])
def listar_gastos():
    gastos = session.query(Gasto).all()
    gastos_serializados = []
    for gasto in gastos:
        gasto_serializado = {
            'gasto_id': gasto.gasto_id,
            'descricao': gasto.descricao,
            'valor': gasto.valor,
            'data': gasto.data.isoformat()  # Converta a data para uma string ISO
        }
        gastos_serializados.append(gasto_serializado)
    return jsonify(gastos_serializados)


@app.route('/gastos/<int:gasto_id>', methods=['PUT'])
def atualizar_gasto(gasto_id):
    gasto = session.query(Gasto).filter_by(gasto_id=gasto_id).first()
    if not gasto:
        return jsonify({"error": "Gasto não encontrado"}), 404

    dados_atualizados = request.json
    descricao = dados_atualizados.get('descricao')
    valor = dados_atualizados.get('valor')

    if descricao:
        gasto.descricao = descricao
    if valor:
        gasto.valor = valor

    try:
        session.commit()
        return jsonify({"message": "Gasto atualizado com sucesso", "gasto_id": gasto.gasto_id})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/gastos/<int:gasto_id>', methods=['DELETE'])
def excluir_gasto(gasto_id):
    gasto = session.query(Gasto).filter_by(gasto_id=gasto_id).first()
    if not gasto:
        return jsonify({"error": "Gasto não encontrado"}), 404

    try:
        session.delete(gasto)
        session.commit()
        return jsonify({"message": "Gasto excluído com sucesso"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
