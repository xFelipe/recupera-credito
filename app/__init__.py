from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serealizer import configure as config_ma


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    # from .pessoa import bp_pessoas
    # app.register_blueprint(bp_pessoas)

    from .pessoa_fisica import bp_pessoas_fisicas
    app.register_blueprint(bp_pessoas_fisicas)

    from .pessoa_juridica import bp_pessoas_juridicas
    app.register_blueprint(bp_pessoas_juridicas)
    
    return app
