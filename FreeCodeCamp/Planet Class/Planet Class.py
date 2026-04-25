class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star
        
        if not isinstance(self.name, str) or not isinstance(self.planet_type, str) or not isinstance(self.star, str):
            raise TypeError("Name, planet type, and star must be strings.")
        if self.name == "" or self.planet_type == "" or self.star == "":
            raise ValueError("Name, planet type, and star must be non-empty strings.")
    
    def orbit(self):
        return f"{self.name} is orbitting around {self.star}...."
    
    def __str__(self):
        return f"Planet : {self.name} | Type : {self.planet_type} | Star : {self.star}"
    
    
Planet_1 = Planet("Earth", "Terrestrial", "Sun")
Planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
Planet_3 = Planet("Mars", "Terrestrial", "Sun")

print(Planet_1.orbit())
print(Planet_1.__str__())
print(Planet_2.orbit())
print(Planet_2.__str__())
print(Planet_3.orbit())
print(Planet_3.__str__())

