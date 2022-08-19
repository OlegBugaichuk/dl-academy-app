from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from src.core.settings import (ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM,
                               SECRET_KEY)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hash(raw_string: str) -> str:
    return pwd_context.hash(raw_string)


def verify_hash(raw_string: str, hash: str) -> bool:
    return pwd_context.verify(raw_string, hash)


def create_access_token(data: dict,
                        expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
