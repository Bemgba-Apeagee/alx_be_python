class Book:
    """Base class representing a generic book."""

    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a readable string representation of the book."""
        return f"{self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize an eBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        """Return a readable string representation of the eBook."""
        return f"{self.title} by {self.author} (E-Book, {self.file_size}MB)"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize a print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a readable string representation of the print book."""
        return f"{self.title} by {self.author} (Print Book, {self.page_count} pages)"


class Library:
    """A class representing a library that holds a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library has no books yet.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f" - {book}")
