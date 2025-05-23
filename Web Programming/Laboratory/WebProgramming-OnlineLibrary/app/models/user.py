from sqlmodel import SQLModel, Field
from datetime import date


class BaseUser(SQLModel):
    name: str
    birth_date: date
    city: str
   
   
class User(BaseUser, table=True): #table = True indica che questa classe rappresenta una tabella nel database
    id: int | None = Field(default=None, primary_key=True)  # ID univoco per ogni utente messo a opzionale perchè non è necessario specificarlo lo crea il db
    
    
class UserPublic(BaseUser):
    pass