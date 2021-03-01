
pessoa_juridica = {'nome': 'Pessoa juridica teste', 'cnpj': '592915340001'}

def test_status_code_200_ao_listar_pessoas_juridicas(client):
    assert client.get('/pessoas_juridicas').status_code == 200

def test_lista_de_pessoas_juridicas_vazia(client):
    assert client.get('/pessoas_juridicas').json == []

def test_cadastro_pessoa_juridica(client):
    response = client.post('/pessoa_juridica', json=pessoa_juridica)
    assert response.status_code == 201
    assert response.json.get('nome') == pessoa_juridica['nome']
    assert response.json.get('cnpj') == pessoa_juridica['cnpj']

def test_mostra_pessoa_juridica(client):
    client.post('/pessoa_juridica', json=pessoa_juridica)
    response = client.get('/pessoa_juridica/1')
    assert response.status_code == 200
    assert response.json.get('nome') == pessoa_juridica['nome']
    assert response.json.get('cnpj') == pessoa_juridica['cnpj']

def test_altera_pessoa_juridica(client):
    novos_dados = {'nome': 'novo nome', 'cnpj': '40028922999'}
    client.post('/pessoa_juridica', json=pessoa_juridica)
    response = client.put(f'/pessoa_juridica/1', json=novos_dados).get_json()
    assert response['nome'] == novos_dados['nome']
    assert response['cnpj'] == novos_dados['cnpj']

def test_deleta_pessoa_juridica(client):
    client.post('/pessoa_juridica', json=pessoa_juridica)
    delete_request = client.delete('/pessoa_juridica/1')
    assert delete_request.status_code == 200
    assert not client.get(f'/pessoas_juridicas').get_json()
