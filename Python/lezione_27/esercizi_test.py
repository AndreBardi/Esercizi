"""class Member:
    def __init__(self, member_id: str, name: str, borrowed_books: list) -> None:
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list[Book] = borrowed_books
    
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

class Book:
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool) -> None:
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = is_borrowed

    def borrow():
        pass

class Library:
    pass"""

def transform(x: int) -> int:
    
    if x % 2 == 0:
        num = x / 2
    if x % 2 != 0:
        num = x * 3- 1
    return num

print(transform(4))
print(transform(3))
print(transform(0))
print(transform(-10))
print(transform(-5))