from fastapi import APIRouter

from app.auth.schemas import RegisterUser

router = APIRouter(prefix="/auth", tags=["auth"])



@router.post("/register-user")
def register_user(user: RegisterUser):
    pass
