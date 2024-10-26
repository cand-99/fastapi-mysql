from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base
from .user_model import User
import enum
from datetime import datetime

class Gender(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    address = Column(String(255))
    age = Column(Integer)
    gender = Column(Enum(Gender))
    birth_date = Column(Date)
    phone_number = Column(String(20))
    bio = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="profile")

User.profile = relationship("Profile", back_populates="user", uselist=False)
