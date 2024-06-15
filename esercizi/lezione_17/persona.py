class Persona:
    def __init__(self, first_name: str, last_name: str) -> None:
        if type(first_name) is str:
            self.first_name = first_name
        else:
            self.first_name = None
            print("Il nome inserito non è una stringa!")

        if type(last_name) is str:
            self.last_name = last_name
        else:
            self.last_name = None
            print("Il nome inserito non è una stringa!")

        if first_name is not None and last_name is not None:
            self.età = 0
        else:
            self.età = None
    
    def setName(self, first_name):
       if type(first_name) is str:
           self.first_name = first_name
       else:
           print("Il nome inserito non è una stringa!")
    
    def setLastName(self, last_name):
        if type(last_name) is str:
            self.last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")

    def setAge(self, età):
        if type(età) is int:
            self.età = età
        else:
            print("L'età deve essere un numero intero!")

    def getName(self):
        return self.first_name
    
    def getLastname(self):
        return self.last_name
    
    def getAge(self):
        return self.età
    
    def greet(self):
        print(f'Ciao, sono {self.first_name} {self.last_name}! Ho {self.età} anni!')
