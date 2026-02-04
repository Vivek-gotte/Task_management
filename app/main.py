from fastapi import FastAPI
from app.database import Base, engine

from app.models.models import User
from app.models.models import Task
from app.models.models import Role
from app.models.models import Permission
from app.routers import auth, tasks, users

from fastapi.middleware.cors import CORSMiddleware



Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(users.router)
