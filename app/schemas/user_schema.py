from pydantic import BaseModel, EmailStr
from app.models.user_model import Role
from datetime import datetime
from app.schemas.profile_schema import ProfileCreate, ProfileUpdate, Profile

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    password: str
    profile: ProfileCreate | None = None
    
class UserUpdate(BaseModel):
    email: EmailStr | None = None
    name: str | None = None
    password: str | None = None
    avatar: str | None = None
    role: Role | None = None
    is_active: bool | None = None
    verified_email: bool | None = None
    profile: ProfileUpdate | None = None

class User(UserBase):
    id: int
    avatar: str | None = None
    role: Role
    provider_id: str | None = None
    is_active: bool
    verified_email: bool
    reset_password_token: str | None = None
    reset_password_expires: datetime | None = None
    email_comfirmation_token: str | None = None
    email_confirmation_expires: datetime | None = None
    created_at: datetime
    updated_at: datetime
    profile: Profile | None = None

    class Config:
        from_attributes = True
