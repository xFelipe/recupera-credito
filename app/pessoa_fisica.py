from flask import Blueprint, current_app, request

from .model import PessoaFisica
from .serealizer import PessoaFisicaSchema

bp_pessoas_fisicas = Blueprint('pessoas_fisicas', __name__)

@bp_pessoas_fisicas.route('/pessoas_fisicas', methods=['GET'])
def listar():
    ps = PessoaFisicaSchema(many=True)
    result = PessoaFisica.query.all()
    return ps.jsonify(result), 200

@bp_pessoas_fisicas.route('/pessoa_fisica/<pessoa_id>', methods=['GET'])
def mostrar(pessoa_id):
    ps = PessoaFisicaSchema(many=False)
    result = PessoaFisica.query.get(pessoa_id)
    return ps.jsonify(result), 200 if result else 404


@bp_pessoas_fisicas.route('/pessoa_fisica/<pessoa_id>', methods=['DELETE'])
def deletar(pessoa_id):
    ps = PessoaFisicaSchema(many=False)
    pessoa = PessoaFisica.query.get(pessoa_id)
    if not pessoa:
        return {"message": "Pessoa não encontrada."}, 404
    current_app.db.session.delete(pessoa)
    current_app.db.session.commit()
    return ps.jsonify(pessoa), 200

@bp_pessoas_fisicas.route('/pessoa_fisica/<pessoa_id>', methods=['PUT'])
def alterar(pessoa_id):
    ps = PessoaFisicaSchema(many=False)
    pessoa = PessoaFisica.query.get(pessoa_id)
    assert pessoa.id
    if not pessoa:
        return {"message": "Pessoa não encontrada."}, 404
    if request.json.get('nome'):
        pessoa.nome = request.json['nome']
    if request.json.get('cpf'):
        pessoa.cpf = request.json['cpf']
    current_app.db.session.add(pessoa)
    current_app.db.session.flush()
    current_app.db.session.commit()
    return ps.jsonify(pessoa), 200

@bp_pessoas_fisicas.route('/pessoa_fisica', methods=['POST'])
def criar():
    ps = PessoaFisicaSchema()
    json_serealized_data = ps.load(request.json)
    pessoa = PessoaFisica(**json_serealized_data)
    # import ipdb; ipdb.set_trace()
    current_app.db.session.add(pessoa)
    current_app.db.session.flush()
    current_app.db.session.commit()
    return ps.jsonify(pessoa), 201
