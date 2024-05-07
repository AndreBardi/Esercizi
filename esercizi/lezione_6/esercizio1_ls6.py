class Student:
    def __init__(self, name: str, studyProgram: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = None
    
    def set_age(self, new_age: int):
        self.age = new_age
    
    def printInfo(self):
        print(f"Name={self.name}, Study Program={self.studyProgram},"\
                +f"Age={self.age}")

    def __str__(self):
        return f'Student(name={self.name},'\
        + f'studyProgram={self.studyProgram},'\
            + f'age={self.age})'

me = Student("Andrea", "Informatics")
myleft = Student("Marco", "Informatics")
myright = Student("Michele", "informatics")

me.printInfo()
myleft.printInfo()
myright.printInfo()
