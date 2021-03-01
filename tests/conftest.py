import os
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/database.db'
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            app.db.drop_all()
            app.db.create_all()
        yield client
