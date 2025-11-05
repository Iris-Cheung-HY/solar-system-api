from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    mass: Mapped[int]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped["Planet"] = relationship(back_populates="moons")


    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "mass": self.mass,
            "planet": self.planet.name if self.planet_id else None,
            "planet_id": self.planet_id
        }
        return moon_as_dict
        


    
    @classmethod
    def from_dict(cls, moon_data):
        planet_id = moon_data.get("planet_id")
        new_moon = cls(name=moon_data["name"],
                        description=moon_data["description"],
                        mass=moon_data["mass"],
                        planet_id=planet_id
        )
        return new_moon
