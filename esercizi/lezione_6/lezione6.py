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

    def open_restaurant(self):
        print(f'Il ristorante {self.name} è aperto')
        self.open = True

    def increment_number(self):
        if self.open:
            self.number_served += 1

    def close_restaurant(self):
        self.number_served = 0
        self.open = False

r1 = Restaurant(name="La vecchia Roma", cuisine_type="Romana")
print(f'Numero_Servizi={r1.number_served}, Ristorante Aperto? {r1.open}')
r1.increment_number()
print(r1.number_served)
r1.open_restaurant()
for _ in range(100):
    r1.increment_number()
print(r1.number_served)
r1.close_restaurant()
print(r1.number_served)

class User:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 age: int,
                 cf: str,
                 email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.cf = cf
        self.email = email

    def greet_user(self):
        print(f"Hello {self.first_name}. Come va?")

    def __str__(self) -> str:
        return f'User(name={self.first_name},'\
            + f'surname={self.last_name})'
    
user1 = User(first_name="Lorenzo",
             age=22, last_name="Maggi",
             email="lorenzo.maggi@gmail.com",
             cf="MGGLNZ01L07H501I")
print(user1)
