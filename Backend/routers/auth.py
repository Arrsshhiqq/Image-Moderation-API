from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from utils import get_database, generate_token, get_admin_token
from models import Token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/tokens", response_model=Token)
async def create_token(is_admin: bool = False, _=Depends(get_admin_token)):
    token_doc = generate_token(is_admin)
    db = get_database()
    db.tokens.insert_one(token_doc)
    return token_doc

@router.get("/tokens", response_model=List[Token])
async def list_tokens(_=Depends(get_admin_token)):
    db = get_database()
    tokens = list(db.tokens.find())
    return tokens

@router.delete("/tokens/{token}")
async def delete_token(token: str, _=Depends(get_admin_token)):
    db = get_database()
    result = db.tokens.delete_one({"token": token})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Token not found")
    return {"detail": "Token deleted"}