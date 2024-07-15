from typing import Tuple

class Person:
    
    def __init__(self,
                 name: str,
                 surname: str,
                 date_of_birth: str,
                 gender: str,) -> None:
          
          self.name: str = name
          self.surname: str = surname
          self.date_of_birth: str = date_of_birth
          self.gender: str = gender
          
    
    def calcola_eta(self) ->  int:
            
            return 10
    
person_1: Person = Person(name="Flavio",
                          surname="Giorgi",
                          date_of_birth="24/12/94",
                          gender="Male",)

class Dipendende(Person):
      
        def __init__(self, 
                   name: str, 
                   surname: str, 
                   date_of_birth: str, 
                   gender: str,
                   ore_lavorate: int) -> None:
                   
            self.ore_lavorate: str = ore_lavorate  
            super().__init__(name, surname, date_of_birth, gender)
        
        def calcola_stipendio(self) -> int:

            return 500

dipendente_1 : Dipendende = Dipendende(name="Flavio",
                          surname="Giorgi",
                          date_of_birth="24/12/94",
                          gender="Male",
                          ore_lavorate=50)

class Professore(Dipendende):
      
      def __init__(self, 
                   name: str, 
                   surname: str, 
                   date_of_birth: str, 
                   gender: str, 
                   ore_lavorate: int,
                   materia_insegnata: str,
                   ore_di_lezione: int) -> None:
                       
            super().__init__(name, surname, date_of_birth, gender, ore_lavorate)

            self.materia_insegnata: str = materia_insegnata
            self.ore_di_lezione: int = ore_di_lezione
        

print(person_1.calcola_eta())

print(dipendente_1.name)
print(dipendente_1.calcola_eta())
print(dipendente_1.calcola_stipendio())
print(dipendente_1.ore_lavorate)    



professore_1: Professore = Professore(name="Flavio",
                          surname="Giorgi",
                          date_of_birth="24/12/94",
                          gender="Male",
                          ore_lavorate=50,
                          materia_insegnata="Python",
                          ore_di_lezione=1000)

print(professore_1.ore_di_lezione)
print(professore_1.materia_insegnata)