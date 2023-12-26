"""
Loo klassid Library, Book, Author. Ning Library klassi meetod, millega saab lisada raamatuid raamatukogusse ning
tagastada ühe autori raamatuid."Lisaks Library klassi meetodid add_book(), mille abil saab raamatuid raamatukogusse
juurde lisada, ning books_by_author(), mis tagastab kõik etteantud autori poolt loodud raamatud raamatukogus.
"""


class Author:
    def __init__(self, name):
        self.name = name


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book):
        if book.author.name not in self.books:
            self.books[book.author.name] = [Book(book.title, book.author, book.year)]
        else:
            self.books[book.author.name].append(Book(book.title, book.author, book.year))

    def books_by_author(self, author):
        if author.name in self.books:
            return self.books[author.name]
        return []


author3 = Author("J.K. Rowling")
author4 = Author("Stephen King")

book4 = Book("Harry Potter and the Philosopher's Stone", author3, 1997)
book5 = Book("The Shining", author4, 1977)
book6 = Book("Harry Potter and the Chamber of Secrets", author3, 1998)

library2 = Library("My Library")
library2.add_book(book4)
library2.add_book(book5)
library2.add_book(book6)

books_by_rowling2 = library2.books_by_author(author3)

print(f"Books by {author3.name} in {library2.name}:")
for book in books_by_rowling2:
    print(f"- {book.title} ({book.year})")
