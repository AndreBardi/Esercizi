#N°1
class Book:
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False

class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self, book):
        for book in self.borrowed_books:
            if book not in self.borrowed_books:
                self.borrowed_books.append(book)
            else:
                return f'error: {book} already taken'
        return self.borrowed_books
    
    def return_book(self, book):
        for book in self.borrowed_books:
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
            else:
                return f'error: {book} is not borrowed'

class Library:
    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
    
    def add_book(self, book_id: str, title: str, author: str):
        if book_id not in self.books:
            self.books[book_id] = Book(book_id=book_id, title=title, author=author)

    def register_member(self, member_id:str, name: str):
        if member_id not in self.members:
            self.members[member_id] = Member(member_id=member_id, name=name)
    
    def borrow_book(self, member_id: str, book_id: str):
        if book_id in self.books and member_id in self.members:
           self.members[member_id].borrow_book(self.books[book_id])
        else:
            return 'Member not found' and 'Book not found' 

    def return_book(self, member_id: str, book_id: str):
        if book_id in self.books and member_id in self.members:
            self.members[member_id].return_book(self.books[book_id])
        else:
            return 'Member not found' and 'Book not found' 

    def get_borrowed_books(self, member_id: str) -> list[Book]:
        if member_id in self.members:
            bor_book: list = []
            for i in self.members[member_id].borrowed_books:
                bor_book.append(i.title)
            return bor_book
 
    

#N°2
"""
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    new_dict = {}
    for key, value in prodotti.items():
        if value >= 20:
            new_dict[key] = value - (value / 10)
    return new_dict"""

#N°3
"""
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    n_dict = {'pari' : [], 'dispari' : []}
    for l in lista:
        if l % 2 == 0:
            n_dict['pari'].append(l)
        else:
            n_dict['dispari'].append(l)
    return n_dict"""

#N°4
"""
def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1, 8):
        print(i)

    print("\nSequenza b):")
    for v in range(3, 28, 5):
        print(v)

    print("\nSequenza c):")
    for x in range(20, -16, -6):
        print(x)

    print("\nSequenza d):")
    for k in range(19, 59, 8):
        print(k)
    
    return"""

#N°5
"""
"""

#N°6
"""
def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    sum = 0
    for e in numbers:
        if e > threshold:
            sum+=e
    return sum"""

#N°7
"""
"""

#N°8
"""
def transform(x: int) -> int:
    if x % 2 == 0:
        num: int = x / 2
    if x % 2 != 0:
        num: int = x * 3- 1
    return num"""

#N°9
"""
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True:
        return 'Operazione permessa'
    elif conditionB and conditionC == True:
        return 'Operazione permessa'
    else:
        return 'Operazione negata'
    return check_combination"""

#N°10
"""
"""

#N°11
"""
"""

#N°12
"""
def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dizionario = {}
    for key, value in tuples:
        if key in dizionario:
            dizionario[key].append(value)
        else:
            dizionario[key] = [value]
    return dizionario"""

#N°13
"""
def frequency_dict(elements: list) -> dict:
    frequency_map = {}
    for element in elements:
        frequency_map[element] = frequency_map.get(element, 0) +1
    return frequency_map"""

#N°14
"""
def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key in dizionario:
        if dizionario[key] == valore:
            return key"""

#N°15
"""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict"""

#N°16
"""
def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and  password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    return check_access"""