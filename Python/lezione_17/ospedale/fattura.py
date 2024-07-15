from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, paziente: list[Paziente], dottore: Dottore) -> None:

        self.dottore: Dottore = dottore
        self.paziente: list[Paziente] = paziente
        
        if dottore.isAValidDoctor():
            self.fatture = len(paziente)
            self.salary = 1
        else:
            dottore = None
            paziente = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura poiché il dottore non è valido!")

    def getSalary(self):
        if self.dottore and self.paziente:
            self.salary = self.dottore.getParcel() * self.fatture
            return self.salary
        return None

    def getFatture(self):
        if self.paziente is not None:
            self.fatture = len(self.paziente)
            return self.fatture
        return None

    def addPatient(self, newPatient):
        
        if self.paziente is not None:
            self.paziente.append(newPatient)
            self.fatture = self.getFatture()
            self.salary = self.getSalary()
            print(f"Alla lista del Dottor {self.dottore.last_name} è stato aggiunto il paziente {newPatient.last_name}")

    def removePatient(self, idCode):
        if self.paziente is not None:
            for i in self.paziente:
                if i.idCode == idCode:
                    self.paziente.remove(i)
                    break
            self.fatture = self.getFatture()
            self.salary = self.getSalary()
            print(f"Alla lista del Dottor {self.dottore.last_name} è stato rimosso il paziente {idCode}")