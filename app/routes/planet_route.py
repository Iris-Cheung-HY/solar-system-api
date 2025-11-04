from flask import Blueprint, abort, make_response, request, Response
from ..models.planet import Planet
from ..models.moon import Moon
from .route_utilities import validate_model, create_model, get_models_with_filters
from ..db import db


bp = Blueprint("planet_bp",__name__,url_prefix="/planets")

# @bp.post("")
# def create_planet():
#     request_body = request.get_json()
#     try:
#         new_planet = Planet.from_dict(request_body)
#     except KeyError as error:
#         response = {"message": f"Invalid request: missing {error.args[0]}"}
#         abort(make_response(response, 400))   
    
#     db.session.add(new_planet)
#     db.session.commit()

#     return new_planet.to_dict(), 201


# @bp.get("")
# def get_all_planets():
#     # create a basic select query without any filtering
#     query = db.select(Planet)

#     # If we have a `name` query parameter, we can add on to the query object
#     name_param = request.args.get("name")
#     if name_param:
#         query = query.where(Planet.name.ilike(f"%{name_param}%"))
        
#     description_param = request.args.get("description")
#     if description_param:
#         # In case there are planets with similar names, we can also filter by description
#         query = query.where(Planet.description.ilike(f"%{description_param}%"))

#     planets = db.session.scalars(query.order_by(Planet.id))

#     response = []

#     for planet in planets: 
#         response.append(planet.to_dict())     
        
#     return response

# @bp.get("/<id>")
# def get_single_planet(id):
#     planet = validate_model(Planet, id)
#     return planet.to_dict()

# @bp.put("/<id>")
# def update_planet(id):
#     planet = validate_model(Planet, id)
#     request_body = request.get_json()
#     planet.mass = request_body["mass"]
#     planet.name = request_body["name"]
#     planet.description = request_body["description"]
#     db.session.commit()

#     return Response(status=204, mimetype="application/json")

# @bp.delete("/<id>")
# def delect_planet(id):
#     planet = validate_model(Planet, id)
#     db.session.delete(planet)
#     db.session.commit()
#     return Response(status=204, mimetype="application/json")

@bp.post("")
def create_planet():
    request_body = request.get_json()
    return create_model(Planet, request_body)




@bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)

@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

@bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.mass = request_body["mass"]
    db.session.commit()

    return Response(status=204, mimetype="application/json") # 204 No Content

@bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.post("/<planet_id>/moons")
def create_moon_with_planet(planet_id):
    planet = validate_model(Planet, planet_id)   
    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    return create_model(Moon, request_body)

@bp.get("/<planet_id>/moons")
def get_moons_by_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    response = [moon.to_dict() for moon in planet.moons]
    return response
