# Image Moderation API

A FastAPI-based API for moderating images with bearer token authentication and a Dockerized frontend.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Image-Moderation-API

2. Install Backend Dependencies
   cd Backend
   pip install -r requirements.txt

3. Set up environment variables: Copy .env.example to .env and update values

4. Run with Docker:
  docker compose up --build

5. Access the API at http://localhost:7000/docs and the frontend at http://localhost:8000.

API Endpoints
POST /auth/tokens: Create a new token (admin-only).
GET /auth/tokens: List all tokens (admin-only).
DELETE /auth/tokens/{token}: Delete a token (admin-only).
POST /moderate: Upload an image for moderation.

Running Locally

cd Backend
uvicorn main:app --host 0.0.0.0 --port 7000 --reload
cd Frontend
python -m http.server 8000