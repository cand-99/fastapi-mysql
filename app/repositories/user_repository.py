from sqlalchemy.orm import Session
from app.models.user_model import User as UserModel
from app.schemas.user_schema import UserCreate, UserUpdate
from app.models.user_model import Role

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def create(self, user: UserCreate, hashed_password: str):
        db_user = UserModel(
            email=user.email,
            name=user.name,
            password=hashed_password,
            role=Role.ADMIN,  # You might want to adjust this based on your requirements
            is_active=True,
            verified_email=False
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(UserModel).offset(skip).limit(limit).all()

    def get_by_id(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()
    
    def update(self, user_id: int, user_update_data: dict):
            db_user = self.get_by_id(user_id)
            if db_user:
                for key, value in user_update_data.items():
                    setattr(db_user, key, value)
                self.db.commit()
                self.db.refresh(db_user)
            return db_user

    def delete(self, user_id: int):
        db_user = self.get_by_id(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return db_user