from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod

    def codifica(self, testoInChiaro):
        pass