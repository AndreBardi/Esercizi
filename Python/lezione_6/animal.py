class Animal:
    def __init__(self, name: str, legs: str):
        self.name = name
        self.legs = legs
    
    def set_legs(self, legs):
        self.legs = legs
    
    def get_legs(self):
        return self.legs
         
    def printInfo(self):
        print(f"name={self.name}, nuber of legs={self.legs}")


lion = Animal("Lion", 4)
eagle = Animal("Eagle", 2)
"\n"
print(lion.name)
print(eagle.name)
"\n"
lion.set_legs(3.5)
eagle.set_legs(1)
"\n"
print(lion.get_legs())
print(eagle.get_legs())
"\n"
lion.printInfo()
eagle.printInfo()

