from flask import Flask
from .db import db, migrate
from .models.planet import Planet
from .routes.planet_route import planet_bp


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/planet_development'

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(planet_bp)

    return app
