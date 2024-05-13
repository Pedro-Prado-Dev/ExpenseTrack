from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isso habilita o CORS para todos os endpoints da aplicação


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/gastos', methods=['GET', 'POST'])
def gastos():
    if request.method == 'GET':
        # Lógica para retornar os gastos existentes
        return jsonify({"message": "Lista de gastos"})
    elif request.method == 'POST':
        # Lógica para adicionar um novo gasto
        novo_gasto = request.json  # Obter os dados do JSON enviado
        # Lógica para adicionar o gasto ao banco de dados
        return jsonify({"message": "Novo gasto adicionado com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)
