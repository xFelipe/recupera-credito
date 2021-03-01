from flask import Blueprint, current_app, request
from sqlalchemy.exc import InvalidRequestError

from .model import Pessoa
from .serealizer import PessoaSchema

bp_pessoas = Blueprint('pessoas', __name__)


@bp_pessoas.route('/pessoas', methods=['GET'])
def listar():
    ps = PessoaSchema(many=True)
    result = Pessoa.query.all()
    return ps.jsonify(result), 200


@bp_pessoas.route('/pessoa/<pessoa_id>', methods=['GET'])
def mostrar(pessoa_id):
    ps = PessoaSchema(many=False)
    result = Pessoa.query.get(pessoa_id)
    return ps.jsonify(result), 200 if result else 404


@bp_pessoas.route('/pessoa/<pessoa_id>', methods=['DELETE'])
def deletar(pessoa_id):
    ps = PessoaSchema(many=False)
    pessoa = Pessoa.query.get(pessoa_id)
    if not pessoa:
        return {"message": "Pessoa não encontrada."}, 404
    current_app.db.session.delete(pessoa)
    current_app.db.session.commit()
    return ps.jsonify(pessoa), 200


@bp_pessoas.route('/pessoa/<pessoa_id>', methods=['PUT'])
def alterar(pessoa_id):
    ps = PessoaSchema(many=False)
    pessoa = Pessoa.query.get(pessoa_id)
    if not pessoa:
        return {"message": "Pessoa não encontrada."}, 404
    try:
        pessoa.query.update(request.json)
    except InvalidRequestError as err:
        return {'message': 'Campos ou valores inválidos foram enviados.'}, 400

    current_app.db.session.commit()
    return ps.jsonify(pessoa), 200


@bp_pessoas.route('/pessoa', methods=['POST'])
def criar():
    ps = PessoaSchema()
    json_serealized_data = ps.load(request.json)
    pessoa = Pessoa(**json_serealized_data)
    current_app.db.session.add(pessoa)
    current_app.db.session.commit()
    return ps.jsonify(pessoa), 201
