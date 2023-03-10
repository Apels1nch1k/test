from pydantic import BaseModel

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    firstName: str
    lastName: str
    email: str
    password: str

class User(UserBase):
    id: int
    firstName: str
    lastName: str
    email: str

    class Config:
        orm_mode = True



class AnimalTypeBase(BaseModel):
    pass
class AnimalTypeCreate(AnimalTypeBase):
    type: str

class AnimalType(AnimalTypeBase):
    id: int
    type: str

    class Config:
        orm_mode = True

