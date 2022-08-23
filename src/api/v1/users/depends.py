from fastapi import Depends
from fastapi.security import (HTTPAuthorizationCredentials as HTTP_A_C,
                              HTTPBearer)
from jose import JWTError, jwt
from src.core.settings import ALGORITHM, SECRET_KEY
from src.crud.users import get_user_by_email
from src.schemas.users import User
from .exceptions import CREDENTIALS_EXCEPTION


security = HTTPBearer()


async def get_current_user(credentials: HTTP_A_C = Depends(security)) -> User:
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise CREDENTIALS_EXCEPTION
    except JWTError:
        raise CREDENTIALS_EXCEPTION
    user = await get_user_by_email(email)
    if user is None:
        raise CREDENTIALS_EXCEPTION
    return user


