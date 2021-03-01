from flask import Blueprint, current_app, request

from .model import PessoaJuridica
from .serealizer import PessoaJuridicaSchema

bp_pessoas_juridicas = Blueprint('pessoas_juridicas', __name__)

@bp_pessoas_juridicas.route('/pessoas_juridicas', methods=['GET'])
def listar():
    pj = PessoaJuridicaSchema(many=True)
    result = PessoaJuridica.query.all()
    return pj.jsonify(result), 200

@bp_pessoas_juridicas.route('/pessoa_juridica/<pessoa_id>', methods=['GET'])
def mostrar(pessoa_id):
    pj = PessoaJuridicaSchema(many=False)
    result = PessoaJuridica.query.get(pessoa_id)
    return pj.jsonify(result), 200 if result else 404


@bp_pessoas_juridicas.route('/pessoa_juridica/<pessoa_id>', methods=['DELETE'])
def deletar(pessoa_id):
    pj = PessoaJuridicaSchema(many=False)
    pessoa = PessoaJuridica.query.get(pessoa_id)
    if not pessoa:
        return {"message": "Pessoa não encontrada."}, 404
    current_app.db.session.delete(pessoa)
    current_app.db.session.commit()
    return pj.jsonify(pessoa), 200

@bp_pessoas_juridicas.route('/pessoa_juridica/<pessoa_id>', methods=['PUT'])
def alterar(pessoa_id):
    pj = PessoaJuridicaSchema(many=False)
    pessoa = PessoaJuridica.query.get(pessoa_id)
    assert pessoa.id
    if not pessoa:
        return {"message": "Pessoa não encontrada."}, 404
    if request.json.get('nome'):
        pessoa.nome = request.json['nome']
    if request.json.get('cnpj'):
        pessoa.cnpj = request.json['cnpj']
    current_app.db.session.add(pessoa)
    current_app.db.session.flush()
    current_app.db.session.commit()
    return pj.jsonify(pessoa), 200

@bp_pessoas_juridicas.route('/pessoa_juridica', methods=['POST'])
def criar():
    pj = PessoaJuridicaSchema()
    json_serealized_data = pj.load(request.json)
    pessoa = PessoaJuridica(**json_serealized_data)
    current_app.db.session.add(pessoa)
    current_app.db.session.flush()
    current_app.db.session.commit()
    return pj.jsonify(pessoa), 201
