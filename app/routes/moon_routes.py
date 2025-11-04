from flask import Blueprint, request, make_response, abort
from app.models.moon import Moon
from app.models.planet import Planet
from ..db import db
from .route_utilities import create_model, get_models_with_filters, validate_model
bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

@bp.post("")
def create_moon():
    request_body = request.get_json()
    return create_model(Moon, request_body)

@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moon, request.args)



# @bp.post("/<moon_id>/planets")
# def create_planet_with_moon(moon_id):
#     moon = validate_model(Moon, moon_id)   
#     request_body = request.get_json()
#     request_body["moon_id"] = moon.id

#     return create_model(Planet, request_body)

# @bp.get("/<moon_id>/planets")
# def get_planets_by_moon(moon_id):
#     moon = validate_model(Moon, moon_id)
#     response = [planet.to_dict() for planet in moon.planets]
#     return response
