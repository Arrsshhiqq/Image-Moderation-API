from fastapi import FastAPI
from routers import auth, moderate

app = FastAPI(title="Image Moderation API")
app.include_router(auth.router)
app.include_router(moderate.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}