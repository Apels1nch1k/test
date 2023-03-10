from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)

class AnimalType(Base):

    __tablename__ = "animaltype"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String,)
