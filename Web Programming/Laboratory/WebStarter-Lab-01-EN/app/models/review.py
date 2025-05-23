# === DATA MODEL FOR A REVIEW ===

# Import the necessary components for validation
from pydantic import BaseModel, Field  # BaseModel for defining models, Field for validation
from typing import Annotated  # For enriching types with metadata and validation


# Definition of the Review class that represents a book review/rating
class Review(BaseModel):
    # 'review' field that represents the numerical rating:
    # - Can be an integer from 1 to 5 (ge=1 means >=1, le=5 means <=5)
    # - Can be None (no rating)
    # - The default value is None
    review: Annotated[int | None, Field(ge=1, le=5)] = None