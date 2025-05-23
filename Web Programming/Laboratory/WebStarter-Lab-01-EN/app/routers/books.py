# === FILE FOR BOOK API MANAGEMENT ===
# This file defines all routes (endpoints) related to book management
# with base path /books

# Imports for error handling
from fastapi.exceptions import RequestValidationError
from requests import RequestException

# Imports of data models and "databases"
from models.book import Book
from models.review import Review
from data.books import books

# Imports of FastAPI utilities
# - APIRouter: Allows organizing routes in logical groups
# - HTTPException: For generating meaningful HTTP errors
# - Path: For validating and documenting path parameters
from fastapi import APIRouter, HTTPException, Path
# ValidationError: For handling validation errors for submitted data
from pydantic import ValidationError
# Annotated: For adding metadata to types (used for documentation and validation)
from typing import Annotated

# === ROUTER CONFIGURATION ===
# Creation of the router for book management
# prefix="/books": Specifies that all defined routes will have the /books prefix
# (e.g. /books/, /books/1, etc.)
router = APIRouter(prefix="/books")

# === ROUTE DEFINITIONS (ENDPOINTS) ===

# --- GET: Get all books ---
@router.get("/")
def get_all_books(
        sort: bool = False  # Optional parameter to sort books by review
) -> list[Book]:  # The function will return a list of Book objects
    if sort:
        # If the sort parameter is True, sort books by review value
        # The lambda function indicates to use the 'review' field for sorting
        return sorted(books.values(), key=lambda book: book.review) #sorted is a function that sorts a list of elements (books.values()) based on a key (lambda book: book.review)

    # Otherwise, returns all books without sorting
    # Converts the values of the 'books' dictionary into a list
    return list(books.values())

# --- GET: Get a specific book by ID ---
@router.get("/{id}")  # {id} is a path parameter (URL)
def get_book_by_id(id: Annotated[int, Path(description="The ID of the book to search for")]
                   ) -> Book:
    """
    Returns the book with the specified ID
    """
    try:
        return books[id]  # Looks for the book in the dictionary using the ID as a key
    except KeyError:
        # If the book doesn't exist (key not found), generates a 404 error (Not Found)
        raise HTTPException(status_code=404, detail="Book not found")

# --- POST: Add a review to an existing book ---
@router.post("/{id}/review")
def add_review(
    id: Annotated[int, Path(description="The ID of the book to review")],
    review: Review  # This parameter is automatically extracted from the JSON request body
):
    """
    Adds a review (rating from 1 to 5) to the book with the specified ID
    """
    try:
        # Updates the book's review field with the provided value
        books[id].review = review.review
        return "Review added successfully"
    except KeyError:
        # If the book doesn't exist, generates a 404 error
        raise HTTPException(status_code=404, detail="Book not found")

# --- POST: Add a new book ---
@router.post("/")
def add_book(book: Book):  # The Book object is automatically deserialized from JSON
    """
    Adds a new book to the collection
    """
    # Checks if a book with the same ID already exists
    if book.id in books:
        # If it exists, generates a 403 error (Forbidden)
        raise HTTPException(status_code=403, detail="A book with this ID already exists")
    
    # Otherwise, adds the book to the dictionary
    books[book.id] = book
    return "Book added successfully"

# --- PUT: Update an existing book ---
@router.put("/{id}")
def update_book(
    id: Annotated[int, Path(description="The ID of the book to update")],
    book: Book  # Updated book data from the request body
):
    """
    Updates the data of an existing book
    """
    # Checks if the book exists
    if not id in books:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Updates the book data
    books[id] = book
    return "Book updated successfully"

# --- DELETE: Delete all books ---
@router.delete("/")
def delete_all_book():
    """
    Deletes all books from the collection
    """
    books.clear()  # Empties the dictionary
    return "All books have been successfully deleted"

# --- DELETE: Delete a specific book ---
@router.delete("/{id}")
def delete_book(
    id: Annotated[int, Path(description="The ID of the book to delete")]
):
    """
    Deletes the book with the specified ID
    """
    try:
        del books[id]  # Deletes the element from the dictionary
        return "Book deleted successfully"
    except KeyError:
        # If the book doesn't exist, generates a 404 error
        raise HTTPException(status_code=404, detail="Book not found")