# library_management.py

class Book:
    """Represents a book with title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book."""
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} ({status})"


class Library:
    """Represents a library that stores and manages books."""

    def __init__(self):
        self._books = []  # private list to hold Book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False

    def check_out_book(self, title):
        """Check out a book by its title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"You have checked out '{title}'."
        return f"'{title}' is not available."

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"'{title}' has been returned."
        return f"'{title}' was not checked out."

    def list_available_books(self):
        """Return a list of available books."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            return "No books available."
        return "\n".join(str(book) for book in available)
