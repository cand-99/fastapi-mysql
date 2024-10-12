from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user_schema import User, UserCreate, UserUpdate
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, service: UserService = Depends(get_user_service)):
    return service.get_users(skip, limit)

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(user_id)
    
@router.patch("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, user_service: UserService = Depends(get_user_service)):
    return user_service.update_user(user_id, user)
    
@router.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    return user_service.delete_user(user_id)
