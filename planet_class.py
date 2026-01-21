# freeCodeCamp Python Certification
# Lab: Build a Planet Class
# Author: R.K.Swetha

class Planet:
    
    def __init__(self,name,planet_type,star):

        args = [name, planet_type, star]

        if any(not isinstance(arg, str) for arg in args):
            raise TypeError("name, planet type, and star must be strings")

        if any(len(arg) == 0 for arg in args):
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas giant", "Sun")
planet_3 = Planet("Proxima Centauri b", "Exoplanet", "Proxima Centauri")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
