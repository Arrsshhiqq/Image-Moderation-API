from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Token(BaseModel):
    token: str
    isAdmin: bool
    createdAt: datetime
    expiresAt: Optional[datetime] = None

class Usage(BaseModel):
    token: str
    endpoint: str
    timestamp: datetime