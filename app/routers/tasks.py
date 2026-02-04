from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskOut
from app.models.models import Task
from app.core.deps import get_db, get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_task = Task(**task.dict(), owner_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/", response_model=list[TaskOut])
def list_tasks(
    status: str | None = None,
    priority: str | None = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    query = db.query(Task).filter(Task.owner_id == user.id)
    if status:
        query = query.filter(Task.status == status)
    if priority:
        query = query.filter(Task.priority == priority)
    return query.offset(offset).limit(limit).all()

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404)
    return task

@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: str, data: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404)
    for k, v in data.dict().items():
        setattr(task, k, v)
    db.commit()
    return task

@router.delete("/{task_id}")
def delete_task(task_id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404)
    db.delete(task)
    db.commit()
    return {"message": "Deleted"}
