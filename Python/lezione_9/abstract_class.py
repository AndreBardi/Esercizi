from abc import ABC, abstractmethod

class AbcAnimal(ABC):


    @abstractmethod
    def verso():

        pass

class Cane(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome = nome

    def verso(self):
        print("Bau!")

cane_1: Cane = Cane(nome="Pluto")
cane_1.verso()

class Gatto(AbcAnimal):

    def __init__(self, nome) -> None:
        super().__init__()

        self.nome = nome 

    def verso(self):
        print("Miao!")

gatto_1: Gatto = Gatto(nome="Mela")
gatto_1.verso()