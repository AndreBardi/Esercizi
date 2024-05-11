"""
9-1 + 9-2 + 9-4
"""
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

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()

r1.increment_number()
print(r1.number_served)

r1.open_restaurant()
for _ in range(100):
    r1.increment_number()

print(r1.number_served)
r1.close_restaurant()
print(r1.number_served)

"""
9-3 + 9-5. Users: Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.
"""
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
        self.login_attempts = 0
    
    def greet_user(self):
        print(f"Hello {self.first_name}. Come va?")

    
    def __str__(self) -> str:
        return f'User(name={self.first_name},'\
            + f' surname={self.last_name},'\
            + f' age={self.age},'\
            + f' email={self.email},'\
            + f' cf={self.cf})'
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    
user1 = User(first_name="Lorenzo",
             age=22, last_name="Maggi",
             email="lorenzo.maggi@gmail.com",
             cf="MGGLNZ01L07H501I")
print(user1)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Login attempts:", user1.login_attempts)

user1.reset_login_attempts()
print("Login attempts after reset:", user1.login_attempts)

"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. 
Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
Create an instance of IceCreamStand, and call this method. 
"""
class IceCreamStand(Restaurant):
    def __init__(self, 
                 name: str, 
                 cuisine_type: str, 
                 number_served: int = 0, 
                 open: bool = False,):
        super().__init__(name, cuisine_type, number_served, open)
        
        self.flavour = []

    def display_flavours(self):
        print("The flavours available are:")
        for flavour in self.flavour:
            print(flavour)

        self.flavour.append('Stracciatella')
        self.flavour.append('Zabaione')
        self.flavour.append('Cioccolato')

icecream_stand: str = IceCreamStand(name="Gimmy Zabaione", cuisine_type="Ice Cream Shop")

icecream_stand.display_flavours()
