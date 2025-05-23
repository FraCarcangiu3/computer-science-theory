from fastapi import APIRouter
from data.db import SessionDep
from models.user import User, UserPublic
from models.book import Book, BookPublic
from sqlmodel import select
# Importa i modelli User e UserPublic per la gestione degli utenti
from models.book_user_link import BookUserLink



router = APIRouter(prefix="/users")

@router.get("/")
def get_all_users(session: SessionDep)-> list[UserPublic]:
    """Returns the list of available users."""
    # Crea una query SELECT per ottenere tutti gli utenti dalla tabella 'user'
    statement = select(User)
    # Esegue la query e converte il risultato in una lista di oggetti User
    users = session.exec(statement).all()
    return users

@router.get("/{id}/books")
def get_user_books(
        id: int,
        session: SessionDep
) -> list[BookPublic]:
    """Returns the list of books for a specific user."""
    # Crea una query SELECT per ottenere i libri associati a un utente specifico
    statement = select(Book).join(BookUserLink).where(BookUserLink.user_id == id)
    # Esegue la query e converte il risultato in una lista di oggetti Book
    books = session.exec(statement).all()
    return books