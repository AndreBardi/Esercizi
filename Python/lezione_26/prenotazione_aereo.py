from abc import ABC, abstractmethod

class Volo(ABC):
    def __init__(self, codice_volo: str, posti_tot: int) -> None:
        super().__init__()

        self.codice_volo = codice_volo
        self.posti_tot = posti_tot
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto(self):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

class VoloCommerciale(Volo):
    def __init__(self, codice_volo: str, posti_tot: int) -> None:
        super().__init__(codice_volo, posti_tot)

    