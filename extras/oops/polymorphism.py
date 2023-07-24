class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        pass

class FictionBook(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Year: {self.publication_year}"

class NonFictionBook(Book):
    def __init__(self, title, author, publication_year, subject):
        super().__init__(title, author, publication_year)
        self.subject = subject

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Subject: {self.subject}, Year: {self.publication_year}"

class Database:
    def __init__(self):
        self.books = []
        self.categories = {}  # Map book title to its category

    def add_book(self, book):
        self.books.append(book)
        if isinstance(book, FictionBook):
            self.categories[book.title] = "Fiction"
        elif isinstance(book, NonFictionBook):
            self.categories[book.title] = "Non-Fiction"

    def search_book_by_category(self, category):
        return [book for book in self.books if self.categories.get(book.title) == category]