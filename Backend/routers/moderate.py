from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from utils import get_database, get_current_token
from models import Usage
from datetime import datetime
import random

router = APIRouter(prefix="/moderate", tags=["moderate"])

@router.post("/", response_model=dict)
async def moderate_image(file: UploadFile = File(...), token: dict = Depends(get_current_token)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid image format")
    db = get_database()
    usage = Usage(token=token["token"], endpoint="/moderate", timestamp=datetime.utcnow())
    db.usages.insert_one(usage.dict())
    result = {
        "filename": file.filename,
        "content_type": file.content_type,
        "moderation": {
            "graphic_violence": random.uniform(0, 1),
            "explicit_nudity": random.uniform(0, 1),
            "hate_symbols": random.uniform(0, 1),
            "self_harm": random.uniform(0, 1),
            "extremist_propaganda": random.uniform(0, 1)
        }
    }
    return result