from datetime import datetime
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"        # pending , in_progress , completed
    priority: str = "medium"       # low, medium, high


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None

class TaskOut(BaseModel):
    id: str
    title: str
    description: str | None
    status: str
    priority: str
    owner_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
