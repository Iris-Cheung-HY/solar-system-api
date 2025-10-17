class Planet:
    def __init__(self, id, name, description, mass):
        self.id = id
        self.name = name
        self.description = description
        self.mass = mass

planets = [
    Planet(1, "Earth", "diverse life", 5.972),
    Planet(2, "Mars", "red planet", 6.39e23),
    Planet(3, "Mecury", "closet to the sun", 3.30e23)
]