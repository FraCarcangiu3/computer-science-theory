# === EXAMPLE DATA FOR BOOKS ===

# We import the Book model defined in the models/book.py file
from models.book import Book

# Dictionary that simulates a book database
# In a real application, this data would be stored in a real database
# The dictionary key is the book ID, the value is an instance of the Book class
books = {
    # Book with ID 0, title "book zero", author "author zero" and rating 1
    0: Book(id=0, title="book zero", author="author zero", review=1), #0 is the key, the value is the Book instance
    # Book with ID 1, title "book one", author "author one" and rating 2
    1: Book(id=1, title="book one", author="author one", review=2),
    # Book with ID 2, title "book two", author "author two" and rating 5 (maximum)
    2: Book(id=2, title="book two", author="author two", review=5),
}