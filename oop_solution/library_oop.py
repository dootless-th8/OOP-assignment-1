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


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []        

    # In Library
    def add_book(self, book_id, title, author, available_copies):
        """Add a new book to the library"""
        # book = {
        #     'id': book_id,
        #     'title': title,
        #     'author': author,
        #     'available_copies': available_copies,
        #     'total_copies': available_copies
        # }
        self.books.append(Book(book_id, title, author, available_copies))
        print(f"Book '{title}' added successfully!")

    # In Library
    def add_member(self, member_id, name, email):
        """Register a new library member"""
        # member = {
        #     'id': member_id,
        #     'name': name,
        #     'email': email,
        #     'borrowed_books': []
        # }
        self.members.append(Member(member_id, name, email))
        print(f"Member '{name}' registered successfully!")

    # In Library
    def find_book(self, book_id):
        """Find a book by ID"""
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    # In Library
    def find_member(self, member_id):
        """Find a member by ID"""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    # In member
    def borrow_book(self, member_id, book_id):
        """Process a book borrowing transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            print("Error: Member not found!")
            return False
        
        if not book:
            print("Error: Book not found!")
            return False
        
        if book.available_copies <= 0:
            print("Error: No copies available!")
            return False
        
        if len(member.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        
        # Process the borrowing
        # book.available_copies -= 1
        book.borrow_book()
        # member.borrowed_books.append(book_id)
        member.borrow_book(book_id)
        
        transaction = {
            'member_id': member_id,
            'book_id': book_id,
            'member_name': member.name,
            'book_title': book.title
        }
        self.borrowed_books.append(transaction)
        
        print(f"{member.name} borrowed '{book.title}'")
        return True


    def return_book(self, member_id, book_id):
        """Process a book return transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member or not book:
            print("Error: Member or book not found!")
            return False
        
        if book_id not in member.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False
        
        # Process the return
        # book.available_copies += 1
        book.return_book()
        # member.borrowed_books.remove(book_id)
        member.return_book(book_id)

        # Remove from borrowed_books list
        for i, transaction in enumerate(self.borrowed_books):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                self.borrowed_books.pop(i)
                break
        
        print(f"{member.name} returned '{book.title}'")
        return True

    # In Library
    def display_available_books(self):
        """Display all books with available copies"""
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    # In Library
    def display_member_books(self, member_id):
        """Display books borrowed by a specific member"""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")