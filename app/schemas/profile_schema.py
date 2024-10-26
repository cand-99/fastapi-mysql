from pydantic import BaseModel
from datetime import date
from app.models.profile_model import Gender

class UserBase(BaseModel):
    name: str

class ProfileBase(BaseModel):
    address: str | None = None
    age: int | None = None
    gender: Gender | None = None
    birth_date: date | None = None
    phone_number: str | None = None
    bio: str | None = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileWithUser(BaseModel):
    id: int
    bio: str | None = None
    location: str | None = None
    birth_date: date | None = None
    user: UserBase

    class Config:
        from_attributes = True


class Profile(ProfileBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
