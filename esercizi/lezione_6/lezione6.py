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
print("----------------------")
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
print("----------------------")
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



icecream_stand: str = IceCreamStand(name="Gimmy Zabaione", cuisine_type="Ice Cream Shop")
icecream_stand.flavour = ["-Stracciatella", "-Zabaione", "-Cioccolato"]
icecream_stand.display_flavours()
print("----------------------")
"""
9-7 + 9-8 Admin: An administrator is a special kind of user. 
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. 
Add an attribute, privileges, that stores a list of strings like "can add post", 
"can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s set of privileges. 
Create an instance of Admin, and call your method. 
"""
class Privileges:
    def __init__(self, privileges: list[str]):
        self.privileges = privileges

    def show_privileges(self):
        print("Your list of privileges: ")
        for i in self.privileges:
            print(i)

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, cf: str, email: str, privileges: list[str]):
        super().__init__(first_name, last_name, age, cf, email)
        self.privileges = Privileges(privileges)

admin_privileges = Admin(first_name="Andrea",
                         last_name="Bardi",
                         age=20,
                         cf="BRDNDR04A27H501C",
                         email="andrea_bardi@yahoo.com",
                         privileges=["can add post", "can ban users", "can remove post", "can unban users"],)

admin_privileges.privileges.show_privileges()
print("----------------------")
"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. 
Make a separate file that imports Restaurant. 
Make a Restaurant instance, and call one of Restaurant’s methods to show 
that the import statement is working properly.
"""
from esercizio9_10 import Restaurant

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
print("----------------------")

"""
9-11. Imported Admin: Start with your work from Exercise 9-8. 
Store the classes User, Privileges, and Admin in one module. 
Create a separate file, make an Admin instance, and call show_privileges() 
to show that everything is working correctly.
"""
("""from esercizio9_11 import User 
from esercizio9_11 import Privileges
from esercizio9_11 import Admin

print(user1)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Login attempts:", user1.login_attempts)

user1.reset_login_attempts()
print("Login attempts after reset:", user1.login_attempts)
print("----------------------")
admin_privileges.privileges.show_privileges()
print("----------------------")""")

"""
9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin 
classes in a separate module. 
In a separate file, create an Admin instance and call show_privileges() 
to show that everything is still working correctly.
"""
from esercizio9_11 import User 
from esercizio9_11bis import Privileges
from esercizio9_11bis import Admin

print(user1)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Login attempts:", user1.login_attempts)

user1.reset_login_attempts()
print("Login attempts after reset:", user1.login_attempts)
print("----------------------")
admin_privileges.privileges.show_privileges()
print("----------------------")

"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. 
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
Make a 6-sided die and roll it 10 times. 
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

six_sided_die = Die()
print("Rolling 10d6:")
for _ in range(10):
    print(six_sided_die.roll_die())

ten_sided_die = Die(sides=10)

print("\nRolling 10d10:")
for _ in range(10):
    print(ten_sided_die.roll_die())

twenty_sided_die = Die(sides=20)

print("\nRolling 10d20:")
for _ in range(10):
    print(twenty_sided_die.roll_die())
print("----------------------")
"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
Randomly select 4 numbers or letters from the list and  print a message saying that 
any ticket matching these 4 numbers or letters wins a prize.
"""
import random
def generate_ticket():

    lista: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
    return random.sample(lista, 4)

print(f"La sequenza vincente è: {generate_ticket()}")
print("----------------------")
"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. 
Print a message reporting how many times the loop had to run to give you a winning ticket.
"""
import random

def generate_ticket():
    lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
    return random.sample(lottery, k=4)

my_ticket = ['a', 2, 'b', 7]

attempts = 0

while True:
    attempts += 1
    if generate_ticket() == my_ticket:
        break

print(f"Sono stati necessari {attempts} tentativi per vincere con il biglietto {my_ticket}.")