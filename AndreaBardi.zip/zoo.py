class Animal:
    def __init__(self,
                name: str, 
                species: str, 
                age: int, 
                height: float, 
                width: float, 
                preferred_habitat: str):
       
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = round(100 * (1 / age), 3)
        self.area = height * width

class Fence:
    def __init__(self, 
                 area: float, 
                 temperature: float, 
                 habitat: str, ):
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list = []

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
        if animal.area > fence.area or fence.habitat != animal.preferred_habitat:
            None
        else:
            fence.animals.append(animal)
            

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)

    def feed_animal(self, animal: Animal):
        if animal.area >= (animal.height * animal.width):
            animal.health *= 1.01
            animal.height *= 1.02
            animal.width *= 1.02

    def clean(self, fence: Fence):
        occupied_area = sum(animal.area for animal in fence.animals)
        if fence.area == 0:
            return occupied_area
        else: 
            return occupied_area / fence.area

class Zoo:
    def __init__(self,
                 fences: list,
                 zoo_keepers: list):
        
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def describe_zoo(self):
        print("Guardians:")
        for guardian in self.zoo_keepers:
            print(f"ZooKeeper: name={guardian.name}, surname={guardian.surname}, id={guardian.id}")

        print("Fences:")
        for fence in self.fences:
            print(f"Fence: area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat}")
            print("with animals:")
            for animal in fence.animals:
                print(f"Animal: name={animal.name}, species={animal.species}, age={animal.age}, height={animal.height},"
                f" width={animal.width}, health={animal.health}")

        print("#" * 30)

animal1: Animal = Animal(name="Giraffe", species="Camelopardalis", age=6, height=4.2, width=7.5, preferred_habitat="Savannah")
animal2: Animal = Animal(name="Belgian Shepherd Dog", species="Canis lupus", age=4, height= 62.0, width= 40.2, preferred_habitat="Family Yard")
animal3: Animal = Animal(name="Pigeon", species="Columba livia", age=3, height=2.3, width=1.7, preferred_habitat="Plains")

fence1 = Fence(area=100.0, temperature=45.0, habitat="Savannah")
fence2 = Fence(area=72.0, temperature=37.1, habitat="Family Yard")
fence3 = Fence(area=55.5, temperature=29.8, habitat="Plains")

zookeeper = Zoo_keeper(name="Andrea", surname="Bardi", id="BRD2701")

zoo= Zoo(fences=[fence1, fence2, fence3], zoo_keepers=[zookeeper])

print("State of the zoo before adding animals: ")
zoo.describe_zoo()

zookeeper.add_animal(animal1, fence1)
zookeeper.add_animal(animal2, fence2)
zookeeper.add_animal(animal3, fence3)

print("\nState of the zoo after adding animals: ")
zoo.describe_zoo()

zookeeper.remove_animal(animal3, fence3)

print("\nState of the zoo after removing animal: ")
zoo.describe_zoo()

print("\nCleaning the fence number 1: ")
clean_area1 = zookeeper.clean(fence1)
print(f"Area cleaned in fence 1: {clean_area1}")

print("\nCleaning the fence number 2: ")
clean_area2 = zookeeper.clean(fence2)
print(f"Area cleaned in fence 2: {clean_area2}")

print("\nCleaning the fence number 3: ")
clean_area3 = zookeeper.clean(fence3)
print(f"Area cleaned in fence 2: {clean_area3}")

print("\nFinal state of the zoo: ")
zoo.describe_zoo()