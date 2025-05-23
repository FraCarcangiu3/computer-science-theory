from sqlmodel import SQLModel, Field


class BookUserLink(SQLModel, table=True):  # Modello per la tabella di collegamento, table=True indica che questa classe rappresenta una tabella nel database
    """
    Modello per la tabella di collegamento tra libri e utenti.
    Questa tabella rappresenta una relazione molti-a-molti tra libri e utenti.
    """
    book_id: int = Field(foreign_key="book.id", primary_key=True)  # ID del libro, chiave primaria mi serve perchè così non ho duplicati 
    user_id: int = Field(foreign_key="user.id", primary_key=True)  # ID dell'utente, chiave primaria
    