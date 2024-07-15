class Person:
    # - name
    # - surname
    # - age
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
"""
andrea = Person("Andrea", "Bardi", 20)
print(f"Nome = {andrea.name}, Cognome = {andrea.surname}, Età = {andrea.age}")

marco = Person("Marco", "De Stefano", 19)
print(f"Nome = {marco.name}, Cognome = {marco.surname}, Età = {marco.age}")
"""

persons = [Person("Andrea", "Bardi", 20),
           Person("Marco", "De Stefano", 19)
]