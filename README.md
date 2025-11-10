# Library Management
### _This is program is a managing program for library to manage books, members, borrowing, and displaying information regarding available books in the library and borrowed books for a specific member._

* # Files Structure:
    * ### │
    * ### ├── README.md                          # This file
    * ### │
    * ### ├── procedural_version/
    * ### │   ├── library_procedural.py         # Original procedural code
    * ### │   └── test_procedural.py            # Comprehensive test suite
    * ### │
    * ### ├── oop_solution/
    * ### │   ├── library_oop.py                # Student's OOP implementation (to create)
    * ### │   └── test_oop.py                   # Tests for OOP version (to create)
    * ### ├── library_processing_procederal.py  # Nothing, just for the initial upload and for authenticity sake

# Methods;
* ##  Class Book:
    * ### _init__(self, book_id, title, author, available_copies): store all 4 arguments and store total_copies.
    * ### borrow_book(self): When called will subtract an amount out of available_copies.
    * ### return_book(self): When called will add an amount to the available_copies.

* ## Class Member:
    * ### __init__(self, member_id, name, email): store all 3 arguments and store a list variable borrowed_books for keeping the record of how many books has the member borrowed.
    * ### borrow_book(self, book_id): When called will add book_id to the borrowed_book list.
    * ### return_book(self, book_id): When called will remove book_id to the borrowed book list.

* ## Class Library:
* ## _Note: Most methods in this class notified the user what has been processed after running the methods._
    * ### __init__(self): store three variables, self.books: for recording books, self.members: for recording members, and self.borrowed_books: list a log of each members borrowed books.
    * ### add_book(self, book_id, title, author, available_copies): For creating new Book object and store it in self.books.
    * ### add_member(self, member_id, name, email): For creating new Member object then store it in self.members.
    * ### find_book(self, book_id): For finding specific book, according to book_id, in self.books.
    * ### find_member(self, member_id): For finding specific member, according to member_id, in self.members.
    * ### borrow_book(self, member_id, book_id): Is for processing borrowing books. First, it checks whether the book or member exist in Library or else show error text. Second, check whether in availble_copies and borrowed_books, in Book class and Member class respectively, have a value over 0 or it will gave out error. Lastly, it will call borrow_book method from those classes, and, later, create a dict called transaction with keys 'member_id', 'book_id', 'member_name', and 'book_title' with values as the names suggest store it in self.borrowed_books
    * ### return_book(self, member_id, book_id): Is for returning borrowing books. Similar to that of borrow_book just without needing to check if they are zero. Runs a return_book from both classes, then remove the book from repective member from self.borrowed_books.
    * ### display_available_books(self): Display all books with available copies.
    * ### display_member_books(self, member_id): Display books borrowed by a specific member