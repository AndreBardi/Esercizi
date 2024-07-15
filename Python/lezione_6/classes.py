"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(f"Età = {bob.age}")

if bob.age > alice.age:
    print(f"The Oldest has {bob.age} years")
elif bob.age < alice.age:
    print(f"The Oldest has {alice.age} years")

giovi = Person("Giovanni D", 21)
emanuele = Person("Emanuele G", 19)
bardh = Person("Bardh P", 27)

people = [alice, bob, giovi,
          emanuele, bardh]
"""
"""
youngest = None
for i in people:
    if youngest == None:
        youngest = i.age
    if youngest > i.age:
        youngest = i.age
print(youngest)
"""
"""
min_age: float = float('inf')
index_min_age: int = 0
for i, people in enumerate(people):
    if people.age < min.age:
        min.age = people.age
        index_min_age = i
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies: set[str] = set()
    
    def add_hobbies(self, hobbies: list[str]):
        self.hobbies.update(hobbies)
    
    def add_hobby(self, hobby: str):
        self.hobbies.add(hobby)

    def remove_hobby(self, hobby: str):
        if hobby in self.hobbies:
            self.hobbies.remove(hobby)

    def __str__(self) -> str:
        return f'Person(name={self.name}), age={self.age}, hobbies={self.hobbies}'
    
alice = Person("Alice", 47)
bob = Person("Bob", 37)
print(alice)
alice.add_hobbies(["Pallacanestro", "Cricket", "Pallacanestro"])
print(alice)