"""class Contatore:
    def __init__(self, conteggio: int) -> None:
        self.conteggio = conteggio
        conteggio = 0

    def setZero(self):
        pass"""

class Specie:
    def __init__(self, nome: str,
                 popolazione: int,
                 tasso_crescita: float) -> None:
        
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        self.popolazione