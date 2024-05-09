class Zoo:
    def __init__(self,
                 zoo: str, zoo_keepers: str):
        self.zoo: str = zoo
        self.zoo_keepers: str = zoo_keepers

class Animal:
    def __init__(self,
            name: str, species: str, age: int, height: float, 
            width: float, preferred_habitat: str, health: float):
       
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = health

class Fence:
    def __init__(self, area: float, temperature: 
                 float, habitat: str) -> list:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
    
class Zoo_keeper:
    def __init__(self):
        pass