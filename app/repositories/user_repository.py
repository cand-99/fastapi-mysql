from sqlalchemy.orm import Session
from app.models.user_model import User as UserModel
from app.schemas.profile_schema import ProfileWithUser
from app.schemas.user_schema import UserCreate, UserUpdate
from app.models.user_model import Role
from app.models.profile_model import Profile as ProfileModel
from sqlalchemy.orm import Session, joinedload
from app.utils.paginator import Paginator, QueryResult

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
            role=Role.ADMIN,
            is_active=True,
            verified_email=False
        )
        self.db.add(db_user)
        self.db.flush()  # This assigns an id to db_user

        if user.profile:
            db_profile = ProfileModel(user_id=db_user.id, **user.profile.dict())
            self.db.add(db_profile)

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_all(self, page: int, page_size: int) -> QueryResult[UserModel]:
            return Paginator.paginate_query(
                self.db.query(UserModel),
                page,
                page_size
            )

    def get_by_id(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def update(self, user_id: int, user_update_data: dict):
        db_user = self.get_by_id(user_id)
        if db_user:
            profile_data = user_update_data.pop('profile', None)
            for key, value in user_update_data.items():
                setattr(db_user, key, value)

            if profile_data:
                db_profile = self.get_profile(user_id)
                if db_profile:
                    for key, value in profile_data.items():
                        setattr(db_profile, key, value)
                else:
                    db_profile = ProfileModel(user_id=user_id, **profile_data)
                    self.db.add(db_profile)

            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int):
        db_user = self.get_by_id(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return db_user

    def get_profile(self, user_id: int):
            return self.db.query(ProfileModel).filter(ProfileModel.user_id == user_id).first()

    def get_all_profiles_with_users(self, page: int, page_size: int) -> QueryResult[ProfileWithUser]:
            query = self.db.query(ProfileModel).join(UserModel)
            return Paginator.paginate_query(
                query,
                page,
                page_size
            )
