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

