# Library Management System - OOP Style

class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author        
        self.available_copies = available_copies
        self.total_copies = available_copies

    def borrow_book(self):
        self.available_copies -= 1

    def return_book(self):
        self.available_copies += 1

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []


    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        self.borrowed_books.remove(book_id)