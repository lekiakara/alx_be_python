# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: User-friendly description of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Can recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage (can be removed if not required for submission)
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(str(book1))     # Output: 1984 by George Orwell, published in 1949
    print(repr(book1))    # Output: Book('1984', 'George Orwell', 1949)

    # Deleting the object to show destructor in action
    del book1
