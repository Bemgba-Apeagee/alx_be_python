class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        """Initialize the book with title, author, and availability."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    """A class to represent a library that manages books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"'{book.title}' has been checked out.")
                else:
                    print(f"'{book.title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                else:
                    print(f"'{book.title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available at the moment.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
