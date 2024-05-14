import json
from app import app

def test_adicionar_gasto():
    client = app.test_client()
    novo_gasto = {'descricao': 'Compras de mercado', 'valor': 150.0}
    response = client.post('/gastos', json=novo_gasto)
    assert response.status_code == 201

    # Verifica se o gasto foi adicionado corretamente
    dados_resposta = json.loads(response.data)
    assert dados_resposta['message'] == 'Gasto adicionado com sucesso'

def test_listar_gastos():
    client = app.test_client()
    response = client.get('/gastos')
    assert response.status_code == 200

    # Verifica se a resposta contém uma lista de gastos
    dados_resposta = json.loads(response.data)
    assert isinstance(dados_resposta, list)

def test_atualizar_gasto():
    client = app.test_client()
    novo_gasto = {'descricao': 'Compras de mercado', 'valor': 150.0}
    response = client.post('/gastos', json=novo_gasto)
    assert response.status_code == 201

    dados_resposta = json.loads(response.data)
    gasto_id = dados_resposta['gasto_id']

    # Atualiza o gasto recém-adicionado
    gasto_atualizado = {'descricao': 'Compras de mercado semanal', 'valor': 200.0}
    response = client.put(f'/gastos/{gasto_id}', json=gasto_atualizado)
    assert response.status_code == 200

    # Verifica se o gasto foi atualizado corretamente
    dados_resposta = json.loads(response.data)
    assert dados_resposta['message'] == 'Gasto atualizado com sucesso'


def test_excluir_gasto():
    client = app.test_client()
    novo_gasto = {'descricao': 'Compras de mercado', 'valor': 150.0}
    response = client.post('/gastos', json=novo_gasto)
    assert response.status_code == 201

    dados_resposta = json.loads(response.data)
    gasto_id = dados_resposta['gasto_id']

    # Exclui o gasto recém-adicionado
    response = client.delete(f'/gastos/{gasto_id}')
    assert response.status_code == 200

    # Verifica se o gasto foi excluído corretamente
    dados_resposta = json.loads(response.data)
    assert dados_resposta['message'] == 'Gasto excluído com sucesso'
