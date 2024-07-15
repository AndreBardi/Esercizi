class Restaurant:
    def __init__(self,
                 name: str,
                 cuisine_type: str,
                 number_served: int = 0,
                 open: bool = False):
        self.name : str = name
        self.cuisine_type : str = cuisine_type
        self.number_served : str = number_served
        self.open : bool = open

    def describe_restaurant (self):
        print(f'Il ristorante si chiama "{self.name} e il suo tipo di cucina è {self.cuisine_type}')

    def open_restaurant(self):
        print(f'Il ristorante {self.name} è aperto')
        self.open = True

    def increment_number(self):
        if self.open:
            self.number_served += 1

    def close_restaurant(self):
        self.number_served = 0
        self.open = False

r1 = Restaurant(name= "La vecchia Roma", cuisine_type="Romana")
r2 = Restaurant(name= "Carter Oblio", cuisine_type="Gourmet")
r3 = Restaurant(name= "Neko", cuisine_type="Giapponese")
