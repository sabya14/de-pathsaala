class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"


from abc import ABC, abstractmethod


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book):
        pass


class TextDisplay(BookDisplay):
    def display(self, book):
        return f"Title: {book.title}\nAuthor: {book.author}\nYear: {book.publication_year}"


class GraphicalDisplay(BookDisplay):
    def display(self, book):
        # Implementation of graphical display goes here (for simplicity, we'll use a placeholder)
        return f"Graphical Display for: {book.title}"
