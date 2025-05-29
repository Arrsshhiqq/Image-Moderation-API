from fastapi import HTTPException, status, Header, Depends
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_database():
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
    return client["image_moderation"]

import uuid
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def generate_token(is_admin: bool = False) -> dict:
    return {
        "token": str(uuid.uuid4()),
        "isAdmin": is_admin,
        "createdAt": datetime.utcnow()
    }

async def get_current_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    token = authorization.replace("Bearer ", "")
    db = get_database()
    token_doc = db.tokens.find_one({"token": token})
    if not token_doc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found")
    return token_doc

async def get_admin_token(token: dict = Depends(get_current_token)):
    if not token.get("is_admin"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return token

def test_db_connection():
    db = get_database()
    db.test_collection.insert_one({"test": "ok"})
    return db.test_collection.find_one({"test": "ok"})