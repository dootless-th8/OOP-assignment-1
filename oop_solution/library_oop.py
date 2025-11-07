# Library Management System - OOP Style

class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author        
        self.available_copies = available_copies
        self.total_copies = available_copies