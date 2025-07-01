from fastapi import APIRouter, HTTPException
from models import User
from jose import jwt

router = APIRouter()
SECRET_KEY = "secret"
ALGORITHM = "HS256"

@router.post("/login")
def login(user: User):
    if user.username != "admin" or user.password != "admin":
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = jwt.encode({"sub": user.username}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
