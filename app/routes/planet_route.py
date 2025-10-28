from flask import Blueprint, abort, make_response, request, Response
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

@planet_bp.get("/<id>")
def get_single_planet(id):
    planet = validate_planet(id)
    return dict(
        id=planet.id,
        name=planet.name,
        mass=planet.mass,
        description=planet.description
    )

@planet_bp.put("/<id>")
def update_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()
    planet.mass = request_body["mass"]
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planet_bp.delete("/<id>")
def delect_planet(id):
    planet = validate_planet(id)
    db.session.delete(planet)
    db.session.commit()
    return Response(status=204, mimetype="application/json")

def validate_planet(id):
    try:
        planet_id = int(id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))
    
    query = db.select(Planet).where(Planet.id == id)
    planet = db.session.scalar(query)
    
    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))
    
    return planet

