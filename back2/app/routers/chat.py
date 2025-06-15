from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.assistant.assistant import AIAssistant
import logging

router = APIRouter()
assistant = AIAssistant()
logger = logging.getLogger(__name__)

class ChatMessage(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat(message: ChatMessage):
    try:
        logger.info(f"Received chat message: {message.message}")
        response = await assistant.get_response(message.message)
        logger.info(f"AI response: {response}")
        return ChatResponse(response=response)
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 