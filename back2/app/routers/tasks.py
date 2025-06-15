from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Data
from pydantic import BaseModel
from app.assistant.assistant import AIAssistant
from datetime import datetime

router = APIRouter()
assistant = AIAssistant()

class DataResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime 
    
    class Config:
        from_attributes = True
class TaskCreate(BaseModel):
    title: str
    content: str

@router.get("/data", response_model=List[DataResponse])
def get_all_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = db.query(Data).offset(skip).limit(limit).all()
    return data

@router.get("/data/{data_id}", response_model=DataResponse)
def get_data(data_id: int, db: Session = Depends(get_db)):
    data = db.query(Data).filter(Data.id == data_id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data
@router.post("/data", response_model=DataResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_data = Data(
        title=task.title,
        content=task.content,
        created_at=datetime.utcnow()
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@router.post("/generate", response_model=DataResponse)
async def generate_task(prompt: str, db: Session = Depends(get_db)):
    try:
        # Ask AI to generate a task
        ai_response = await assistant.get_response(
            f"Generate a task based on this prompt: {prompt}. "
            "Format the response as a JSON with 'title' and 'content' fields."
        )
        
        # Create new task with AI-generated content
        new_data = Data(
            title=f"AI Generated Task: {prompt[:30]}...",
            content=ai_response,
            created_at=datetime.utcnow()
        )
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating task: {str(e)}") 
