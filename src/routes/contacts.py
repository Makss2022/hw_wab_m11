from typing import List, Annotated

from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactModel, ContactResponse
from src.repository import contacts as repository_contacts

router = APIRouter(prefix='/contacts', tags=["Contacts"])


@router.get("/", response_model=List[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(skip, limit, db)
    return contacts


@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(body, db)


@router.get("/name", response_model=List[ContactResponse])
async def search_contacts_by_name_fragment(
    name: Annotated[str, Query(min_length=3, max_length=50, description='Name fragment:')],
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    contacts = await repository_contacts.search_contacts_by_name(name, skip, limit, db)
    if bool(contacts) is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")
    return contacts


@router.get("/surname", response_model=List[ContactResponse])
async def search_contacts_by_surname_fragment(
    surname: Annotated[str, Query(min_length=3, max_length=50, description='Surname fragment:')],
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    contacts = await repository_contacts.search_contacts_by_surname(surname, skip, limit, db)
    if bool(contacts) is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")
    return contacts


@router.get("/email", response_model=List[ContactResponse])
async def search_contacts_by_email_fragment(
    email: Annotated[str, Query(min_length=3, max_length=150, description='Email fragment:')],
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    contacts = await repository_contacts.search_contacts_by_email(email, skip, limit, db)
    if bool(contacts) is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")
    return contacts


@router.get("/birthday", response_model=List[ContactResponse])
async def search_contacts_birthdays_next_7_days(db: Session = Depends(get_db)):
    contacts = await repository_contacts.search_contacts_by_birthday(db)
    if bool(contacts) is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(body: ContactModel, contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact




