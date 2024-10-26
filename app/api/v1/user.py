from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user_schema import User, UserCreate, UserUpdate
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.pagination import PageParams, PagedResponse
from app.schemas.profile_schema import ProfileWithUser
router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/users/", response_model=PagedResponse[User])
def read_users(page_params: PageParams = Depends(), service: UserService = Depends(get_user_service)):
    return service.get_users(page_params)

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(user_id)

@router.patch("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, user_service: UserService = Depends(get_user_service)):
    return user_service.update_user(user_id, user)

@router.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    return user_service.delete_user(user_id)

@router.get("/profiles/", response_model=PagedResponse[ProfileWithUser])
def read_profiles_with_users(page_params: PageParams = Depends(), service: UserService = Depends(get_user_service)):
    return service.get_profiles_with_users(page_params)
