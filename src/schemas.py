from datetime import date
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    name: str = Field(max_length=50, min_length=3)
    surname: str = Field(max_length=50, min_length=3)
    email: EmailStr
    phone: str = Field('+380501234567', max_length=13, min_length=10)
    birthday: date
    notes: str = Field(min_length=3)


class ContactResponse(ContactModel):
    id: int = 1
    
    class Config:
        orm_mode = True

