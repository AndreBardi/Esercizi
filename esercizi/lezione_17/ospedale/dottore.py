from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name, specialization, parcel):
        super().__init__(first_name, last_name)

        if type(specialization) is str:
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa!")
        
        if type(parcel) is float:
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")
        
    def setSpecialization(self, specialization):
        if type(specialization) is str:
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")
    
    def setParcel(self, parcel):
        if type(parcel) is float:
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")
    
    def getSpecialization(self):
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.età > 30:
            print(f"Doctor {self.first_name} {self.last_name} is valid!")
        else:
            print(f"Doctor {self.first_name} {self.last_name} is not valid!")
    
    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.__specialization}")