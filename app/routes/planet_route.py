from flask import Blueprint
from app.models.planet import planets


planet_bp = Blueprint("planet_bp",__name__,url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "mass": planet.mass
        })
    return planet_response




