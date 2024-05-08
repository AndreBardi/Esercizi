class Zoo:
    def __init__(self,
                 zoo: str, zoo_keepers: str):
        self.zoo: str = zoo
        self.zoo_keepers: str = zoo_keepers

    def animal(self,
            name: str, species: str, age: str, height: str, 
            width: str, preferred_habitat: str, health: str):
        self.name: str = name
        self.species: str = species