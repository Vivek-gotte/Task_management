from pydantic import BaseModel


class PermissionCreate(BaseModel):
    name: str


class PermissionOut(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True
