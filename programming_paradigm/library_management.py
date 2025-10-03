# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out. Return True if successful, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned (available). Return True if successful, False if already available."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        # private list of Book objects
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False

    def _find_book_by_title(self, title):
        """Internal helper: return the Book instance with matching title (exact match), or None."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """Check out the book with the given title. Return True if successful, False otherwise."""
        book = self._find_book_by_title(title)
        if not book:
            return False
        return book.check_out()

    def return_book(self, title):
        """Return the book with the given title. Return True if successful, False otherwise."""
        book = self._find_book_by_title(title)
        if not book:
            return False
        return book.return_book()

    def list_available_books(self):
        """Print all available books, one per line, exactly as: Title by Author"""
        for book in self._books:
            if book.is_available():
                print(str(book))
