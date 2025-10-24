from flask import Blueprint, abort, make_response, request
from ..models.planet import Planet
from ..db import db


planet_bp = Blueprint("planet_bp",__name__,url_prefix="/planets")

@planet_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    mass = request_body["mass"]

    new_planet = Planet(name=name, description=description, mass = mass)

    db.session.add(new_planet)
    db.session.commit()

    planet_response = dict(
        id=new_planet.id,
        name=new_planet.name,
        description=new_planet.description,
        mass=new_planet.mass
    )

    return planet_response, 201


@planet_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    response = []

    for planet in planets:        
        response.append(dict(
            id=planet.id,
            name=planet.name,
            mass=planet.mass,
            description=planet.description
        ))

    return response





# @planet_bp.get("")
# def get_all_planets():
#     planet_response = []
#     for planet in planets:
#         planet_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "mass": planet.mass
#         })
#     return planet_response

# @planet_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "mass": planet.mass
#     }

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         response = {"message": f"planet {planet_id} invalid"}
#         abort(make_response(response, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     response = {"message": f"planet {planet_id} not found"}
#     abort(make_response(response, 404))


