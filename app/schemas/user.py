from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    role_id: str | None = None


class UserOut(BaseModel):
    id: str
    email: EmailStr
    role_id: str | None
    created_at: datetime

    class Config:
        from_attributes = True
