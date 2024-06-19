import time
class FileManager:
    def __init__(self, file_name, mode: str) -> None:        
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):        
       self.file_wrapper = open(self.file_name, self.mode)
       return self.file_wrapper
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file_wrapper.close()

with FileManager(file_name='prova.txt', mode="w") as file:        
    file.write("Ciao")

with open("prova.txt", mode= "a") as file:
    file.write("!")

class Timer:
    def __enter__(self):
        self.time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):        
        print(f'Time Elapsed: {time.time() - self.time}')
        return False
    
def ciao(name: str) -> str:

    print(f'Greetings, {name}')

def salve():
    pass    

def parent():
    print("Sono in parent\n")

    def first_child():
        print("Sono in First Child!")

    return first_child

print(parent())

def decorator(func):
    def wrapper():
        import time

        start = time.time()

        func()

        print(f"Time elapsed: {time.time() - start}")
        
        return wrapper()


def ciao():

    print(f"Ciao!")

ciao()
ciao = decorator(ciao)
ciao()

