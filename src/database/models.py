from sqlalchemy import Column, Integer, String, func, Date
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50))
    email = Column(String(150), unique=True, index=True)
    phone = Column(String(13), unique=True, index=True)
    birthday = Column(Date)
    notes = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
