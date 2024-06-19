import unittest
from dottore import Dottore
from paziente import Paziente
from persona import Persona
from fattura import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Lorenzo", "Nani")

    def test_initialization(self):
        self.assertEqual(self.persona.getName(), "Lorenzo")
        self.assertEqual(self.persona.getLastname(), "Nani")
        self.assertEqual(self.persona.getAge(), 0)

    def test_setName(self):
        self.persona.setName("Maria")
        self.assertEqual(self.persona.getName(), "Maria")

    def test_setLastName(self):
        self.persona.setLastName("Rosa")
        self.assertEqual(self.persona.getLastname(), "Rosa")

    def test_SetAge(self):
        self.persona.setAge(24)
        self.assertEqual(self.persona.getAge(), 24)

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Stefano", "Sasso", "Reumatologo", 150.0)
        self.dottore.setAge(37)

    def test_initialization(self):
        self.assertEqual(self.dottore.getName(), "Stefano")
        self.assertEqual(self.dottore.getLastname(), "Sasso")
        self.assertEqual(self.dottore.getAge(), 37)
        self.assertEqual(self.dottore.getSpecialization(), "Reumatologo")
        self.assertEqual(self.dottore.getParcel(), 150.0)

    def test_isAValidDoctor(self):
        self.dottore.setAge(35)
        self.assertTrue(self.dottore.getAge() > 30)
        self.dottore.setAge(27)
        self.assertFalse(self.dottore.getAge() > 30)

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Andrea", "Birdi", "P015")

    def test_initialization(self):
        self.assertEqual(self.paziente.getName(), "Andrea")
        self.assertEqual(self.paziente.getLastname(), "Birdi")
        self.assertEqual(self.paziente.getIdCode(), "P015")

class TestFattura(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Stefano", "Sasso", "Reumatologo", 150.0)
        self.dottore.setAge(45)
        self.paziente1 = Paziente("Andrea", "Birdi", "P015")
        self.paziente2 = Paziente("Luca", "Cavallo", "P018")
        self.fattura = Fattura([self.paziente1, self.paziente2], self.dottore)

    def test_initialization(self):
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 300.0)

    def test_add_patient(self):
        paziente3 = Paziente("Marco", "Stefani", "P009")
        self.fattura.addPatient(paziente3)
        self.assertEqual(self.fattura.getFatture(), 3)
        self.assertEqual(self.fattura.getSalary(), 450.0)

    def test_remove_patient(self):
        self.fattura.removePatient("P009")
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 150.0)

if __name__ == "__main__":
    unittest.main()