# Base class
class Book:
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, {self.page_count}"
class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return

        # Print only book details, no header line
        for book in self.books:
            print(book)
