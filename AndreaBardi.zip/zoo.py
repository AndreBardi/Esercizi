class Zoo:
    def __init__(self,
                 fences: list,
                 zoo_keepers: str):
        
        self.fences: list = fences
        self.zoo_keepers: str = zoo_keepers

    def describe_zoo(self):
        pass

class Animal:
    def __init__(self,
                name: str, 
                species: str, 
                age: int, 
                height: float, 
                width: float, 
                preferred_habitat: str, 
                health: float):
       
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = health
        self.area = height*width
        

class Fence:
    def __init__(self, 
                 area: float, 
                 temperature: float, 
                 habitat: str, 
                 animal: list[Animal]) -> list:
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animal: list = animal

class Zoo_keeper:
    def __init__(self,
                 name: str,
                 surname: str,
                 id: str):
        
        self.name: str = name
        self.surname: str = surname
        self.id: str = id
        self.fences: list = []
        self.animals: list = []

    def add_animal(self, animal: Animal, fence: Fence):
        
        if animal.area > fence.area:
            None
        elif fence.area != animal.preferred_habitat:
            None
        else:
            fence.animal.append(animal.name)

        

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal.area > fence.area:
            fence.animal.remove(animal)
        elif fence.area != animal.preferred_habitat:
            fence.animal.remove(animal)


    def feed_animal(self,
                    animal: Animal):
        
        self.animal = animal
        