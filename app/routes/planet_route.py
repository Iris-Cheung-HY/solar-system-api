from flask import Blueprint, abort, make_response, request, Response
from ..models.planet import Planet
from .route_utilities import validate_model
from ..db import db


bp = Blueprint("planet_bp",__name__,url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()
    # name = request_body["name"]
    # description = request_body["description"]
    # mass = request_body["mass"]
    try:
    # new_planet = Planet(name=name, description=description, mass = mass)
        new_planet = Planet.from_dict(request_body)
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))   
    
    db.session.add(new_planet)
    db.session.commit()

    # planet_response = dict(
    #     id=new_planet.id,
    #     name=new_planet.name,
    #     description=new_planet.description,
    #     mass=new_planet.mass
    # )

    return new_planet.to_dict(), 201


@bp.get("")
def get_all_planets():
    # create a basic select query without any filtering
    query = db.select(Planet)

    # If we have a `name` query parameter, we can add on to the query object
    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))
        
    description_param = request.args.get("description")
    if description_param:
        # In case there are planets with similar names, we can also filter by description
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    planets = db.session.scalars(query.order_by(Planet.id))

    response = []

    for planet in planets: 
        response.append(planet.to_dict())     
        # response.append(dict(
        #     id=planet.id,
        #     name=planet.name,
        #     mass=planet.mass,
        #     description=planet.description
        # ))

    return response

@bp.get("/<id>")
def get_single_planet(id):
    planet = validate_model(Planet, id)
    return planet.to_dict()

@bp.put("/<id>")
def update_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()
    planet.mass = request_body["mass"]
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.delete("/<id>")
def delect_planet(id):
    planet = validate_model(Planet, id)
    db.session.delete(planet)
    db.session.commit()
    return Response(status=204, mimetype="application/json")



