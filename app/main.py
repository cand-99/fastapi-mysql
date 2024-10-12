from fastapi import FastAPI
from app.api.v1 import user
from app.db.database import engine
from app.models import user_model
user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/api/v1")
