from pydantic import EmailStr
from sqlmodel import SQLModel


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"
 
class UserCreate(SQLModel):
    email :EmailStr
    password:str

class UserRead(SQLModel):
    id:int
    email:EmailStr
    is_active:bool
    role:str