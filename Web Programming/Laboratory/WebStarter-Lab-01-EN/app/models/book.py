# === DATA MODEL FOR A BOOK ===

# We import BaseModel from pydantic which allows us to define data models
# and Field which allows adding constraints and metadata to fields
from pydantic import BaseModel, Field
# We import Annotated which allows adding additional information to types
from typing import Annotated

# Definition of the Book class that represents a book in our system
class Book(BaseModel):
    # Unique numeric identifier of the book
    id: int
    # Title of the book
    title: str
    # Author of the book
    author: str
    # Book review, which can be:
    # - An integer from 1 to 5 (ge=1 means >=1, le=5 means <=5)
    # - None (no review present yet)
    # The default value is None
    review: Annotated[int|None, Field(ge=1, le=5)] = None




