from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, codice_id: str) -> None:
        super().__init__(first_name, last_name)
        if type(codice_id) is str:
            self.codice_id = codice_id
        else:
            self.codice_id = None
            print("Il codice identificativo inserito non è una stringa!")
    
    def setIdCode(self, codice_id):
        if type(codice_id) is str:
            self.codice_id = codice_id
        else:
            print("Il codice identificativo inserito non è una stringa!")
    
    def getIdCode(self):
        return self.codice_id
    
    def patientInfo(self):
        print(f"Paziente: {self.first_name} {self.last_name}\nID: {self.codice_id}")