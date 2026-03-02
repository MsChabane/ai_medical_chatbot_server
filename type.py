from pydantic import BaseModel
from typing import List, Optional


class ChatRequest(BaseModel):
    user_input: str
    thread_id: int = 1

class ChatResponse(BaseModel):
    success: bool
    response: Optional[str] = None
    error: Optional[str] = None

class Checkpoint(BaseModel):
    threads: int

class HistoryResponse(BaseModel):
    messages: List[dict]

class ThreadListResponse(BaseModel):
    threads: List[int]


    