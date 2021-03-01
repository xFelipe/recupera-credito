from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db

class Pessoa(db.Model):
    __tablename__ = 'pessoa'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tipo = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'pessoa',
        'polymorphic_on': tipo
    }

class PessoaFisica(Pessoa):
    __tablename__ = 'pessoa_fisica'
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'pessoa_fisica'
    }

class PessoaJuridica(Pessoa):
    __tablename__ = 'pessoa_juridica'
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), primary_key=True)
    cnpj = db.Column(db.String(14), unique=True)

    __mapper_args__ = {
        'polymorphic_identity': 'pessoa_juridica'
    }
