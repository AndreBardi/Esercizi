from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, paziente: list[str], dottore: str) -> None:

        doctor:Dottore = Dottore()
        doctor.isAValidDoctor