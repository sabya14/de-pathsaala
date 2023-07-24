class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

    def search_book_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def display_all_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Year: {book.publication_year}")
