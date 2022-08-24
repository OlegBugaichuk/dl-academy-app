from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from src.core.settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hash(raw_string: str) -> str:
    return pwd_context.hash(raw_string)


def verify_hash(raw_string: str, hash: str) -> bool:
    return pwd_context.verify(raw_string, hash)


def create_access_token(
        user_email: str,
        expires_delta: int = settings.access_token_expire_minutes) -> str:

    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode = {
        "sub": user_email,
        "exp": expire
    }
    encoded_jwt = jwt.encode(to_encode,
                             settings.secret_key,
                             algorithm=settings.hash_algorithm)
    return encoded_jwt
