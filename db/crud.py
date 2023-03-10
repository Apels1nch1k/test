from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, firstName=user.firstName,lastName=user.lastName, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_animal_type(db: Session, animaltype: str):
    print(animaltype)
    return db.query(models.AnimalType).filter(models.AnimalType.type == animaltype).first()

def get_animaltype(db: Session, skip: int = 0, limit: int = 100):
    return  db.query(models.AnimalType).offset(skip).limit(limit).all()

def create_animaltype(db: Session, animaltype: schemas.AnimalTypeCreate):
    db_animaltype= models.AnimalType(type=animaltype.type)
    db.add(db_animaltype)
    db.commit()
    db.refresh(db_animaltype)
    return db_animaltype

