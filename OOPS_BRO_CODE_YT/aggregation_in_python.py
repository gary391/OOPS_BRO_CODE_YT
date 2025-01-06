"""
Aggregation - Represents a relationship where one object (the whole)
contain references to one or more INDEPENDENT object (the parts)
"""

class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] # Here we need to add the books in the library

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author} "for book in self.books]

# A library can contain books
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# The class Library and books are independent of each other and can exist with out each other.
# We will create book object and add them to the library

library = Library("Seattle Public Library")

book1 = Book("Harry Potter...", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkein")
book3 = Book("The Fellowship of the Ring", "J.K. Rowling")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# print(library.name)
for book in library.list_books():
    print(book)


