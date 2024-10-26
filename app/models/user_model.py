from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime
from app.db.database import Base
import enum
from datetime import datetime
from sqlalchemy.orm import relationship

class Role(enum.Enum):
    ADMIN = "ADMIN"
    SUPERADMIN = "SUPERADMIN"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    name = Column(String(255))
    password = Column(String(255), nullable=True)
    avatar = Column(String(255), nullable=True)
    role = Column(Enum(Role))
    provider_id = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    verified_email = Column(Boolean, default=False)
    reset_password_token = Column(String(255), nullable=True)
    reset_password_expires = Column(DateTime, nullable=True)
    email_comfirmation_token = Column(String(255), nullable=True)
    email_confirmation_expires = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    profile = relationship("Profile", back_populates="user", uselist=False)
