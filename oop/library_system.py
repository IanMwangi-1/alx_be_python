# library_system.py

class Book:
    """Base Book class with title and author."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Digital book with file size in KB."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Printed book with page count."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Composition: library manages a collection of Book (or subclasses)."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("Only Book (or subclasses) can be added to the library.")
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library (one per line)."""
        for book in self.books:
            print(str(book))
