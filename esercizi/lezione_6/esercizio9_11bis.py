from esercizio9_11 import User

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