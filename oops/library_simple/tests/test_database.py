from oops.library_simple.book import Book
from oops.library_simple.library import Library


def test_add_book():
    db = Library()
    book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy")
    db.add_book(book)
    assert len(db.books) == 1


def test_display_all_books():
    db = Library()
    book_1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy")
    book_2 = Book("Introduction to Python", "John Doe", 2021, "Programming")
    db.add_book(book_1)
    db.add_book(book_2)
    assert len(db.books) == 2

# TODO - add test for searching of book by author
# TODO - add test for searching of book by title