import jwt
from datetime import datetime, timedelta

from app.config import settings
from app.auth.models import User


def create_access_token(user_id: int, email: str) -> dict:
    exp = datetime.utcnow() + timedelta(minutes=settings.jwt_access_token_exp_minutes)
    payload = {"user_id": user_id, "email": email, "exp": exp}
    token = jwt.encode(
        payload=payload, key=settings.jwt_secret, algorithm=settings.jwt_algorithm
    )
    return token


def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            jwt=token, key=settings.jwt_secret, algorithms=[settings.jwt_algorithm]
        )

    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        return "invalid jwt"

    user_id = payload.get("user_id")

    return user_id


def get_current_user(token) -> str:
    verify_access_token(token)
    pass
