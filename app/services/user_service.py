from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate
from passlib.context import CryptContext
from app.schemas.pagination import PagedResponse, PageParams, PaginationMeta
from app.schemas.profile_schema import ProfileWithUser
from app.utils.paginator import Paginator
import math

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: UserCreate):
        existing_user = self.user_repository.get_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_password = pwd_context.hash(user.password)
        return self.user_repository.create(user, hashed_password)

    def get_users(self, page_params: PageParams):
        return Paginator.paginate(self.user_repository.get_all(
                page_params.page,
                page_params.page_size
            ))

    def get_user(self, user_id: int):
        user = self.user_repository.get_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def update_user(self, user_id: int, user_update: UserUpdate):
            existing_user = self.user_repository.get_by_id(user_id)
            if existing_user is None:
                raise HTTPException(status_code=404, detail="User not found")

            update_data = user_update.dict(exclude_unset=True)

            if 'password' in update_data:
                update_data['password'] = pwd_context.hash(update_data['password'])

            updated_user = self.user_repository.update(user_id, update_data)
            return updated_user

    def delete_user(self, user_id: int):
        deleted_user = self.user_repository.delete(user_id)
        if deleted_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return deleted_user

    def get_profiles_with_users(self, page_params: PageParams):
        return Paginator.paginate(self.user_repository.get_all_profiles_with_users(
                   page_params.page,
                   page_params.page_size
               ))
