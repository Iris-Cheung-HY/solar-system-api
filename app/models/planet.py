from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    mass: Mapped[int]  
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")


    def to_dict(self):
        
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["mass"] = self.mass
        planet_as_dict["moons"] = self.moons

        return planet_as_dict


    @classmethod
    def from_dict(cls, planet_data):
        moon_id = planet_data.get("moon_id")
        new_planet = cls(
            name=planet_data["name"],
            description=planet_data["description"],
            mass=planet_data["mass"],
            moon_id=moon_id,
        
        )

        return new_planet      

        