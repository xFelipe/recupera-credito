
pessoa_fisica = {'nome': 'Pessoa fisica teste', 'cpf': '12395483752'}

def test_status_code_200_ao_listar_pessoas_fisicas(client):
    assert client.get('/pessoas_fisicas').status_code == 200

def test_lista_de_pessoas_fisicas_vazia(client):
    assert client.get('/pessoas_fisicas').json == []

def test_cadastro_pessoa_fisica(client):
    response = client.post('/pessoa_fisica', json=pessoa_fisica)
    assert response.status_code == 201
    assert response.json.get('nome') == 'Pessoa fisica teste'
    assert response.json.get('cpf') == '12395483752'

def test_mostra_pessoa_fisica(client):
    client.post('/pessoa_fisica', json=pessoa_fisica)
    response = client.get('/pessoa_fisica/1')
    assert response.status_code == 200
    assert response.json.get('nome') == pessoa_fisica['nome']
    assert response.json.get('cpf') == pessoa_fisica['cpf']

def test_altera_pessoa_fisica(client):
    novos_dados = {'nome': 'novo nome', 'cpf': '40028922999'}
    client.post('/pessoa_fisica', json=pessoa_fisica)
    response = client.put(f'/pessoa_fisica/1', json=novos_dados).get_json()
    assert response['nome'] == novos_dados['nome']
    assert response['cpf'] == novos_dados['cpf']

def test_deleta_pessoa_fisica(client):
    client.post('/pessoa_fisica', json=pessoa_fisica)
    delete_request = client.delete('/pessoa_fisica/1')
    assert delete_request.status_code == 200
    assert not client.get(f'/pessoas_fisicas').get_json()
