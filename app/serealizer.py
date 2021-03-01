from flask_marshmallow import Marshmallow
from marshmallow import fields
from .model import Pessoa, PessoaFisica, PessoaJuridica

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class PessoaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pessoa

    id = ma.auto_field()
    nome = ma.auto_field()
    tipo = ma.auto_field()


class PessoaFisicaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PessoaFisica

    id = fields.Int()
    nome = ma.auto_field()
    tipo = ma.auto_field()
    cpf = ma.auto_field()


class PessoaJuridicaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PessoaJuridica

    id = fields.Int()
    nome = ma.auto_field()
    tipo = ma.auto_field()
    cnpj = ma.auto_field()
