from pydantic import BaseModel

# Schema to characterist of user
class UserBase(BaseModel):
    name: str
    age: int

# Schema to creation of user
class UserCreate(UserBase):
    pass

# Schema to default user
class User(UserBase):
    id: int

    class Config:
        orm_mode = True