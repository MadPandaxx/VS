class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, year):
        self.books[title] = {'author': author, 'year': year}

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]

    def view_books(self):
        for title, details in self.books.items():
            print(f"Title: {title}, Author: {details['author']}, Year: {details['year']}")

    def find_book(self, title):
        if title in self.books:
            details = self.books[title]
            print(f"Title: {title}, Author: {details['author']}, Year: {details['year']}")
        else:
            print("Book not found.")

# Create a library instance
library = Library()

# Add books
library.add_book("Book1", "Author1", 2001)
library.add_book("Book2", "Author2", 2002)
# ... add more books as needed

# View all books
library.view_books()

# Find a book
library.find_book("Book1")

# Remove a book
library.remove_book("Book1")