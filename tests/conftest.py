import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from app.models.planet import Planet
from app.models.moon import Moon
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }

    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_saved_planet(app):
    test_planet = Planet(name="Test Planet", description="nothing interesting", mass=2)
    db.session.add(test_planet)
    db.session.commit()        

@pytest.fixture
def one_saved_moon(app):
    # Arrange
    new_moon = Moon(name="Moon1", mass=5, description="bright")
    
    db.session.add(new_moon)
    db.session.commit()