from fastapi import Depends
from fastapi.security import (HTTPAuthorizationCredentials as HTTP_A_C,
                              HTTPBearer)
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.settings import settings
from src.crud.users import get_user_by_email
from src.schemas.users import User
from src.db.depends import get_db

from .exceptions import CREDENTIALS_EXCEPTION


security = HTTPBearer()


async def get_current_user(credentials: HTTP_A_C = Depends(security),
                           db: AsyncSession = Depends(get_db)) -> User:

    try:
        token = credentials.credentials
        payload = jwt.decode(token,
                             settings.secret_key,
                             algorithms=[settings.hash_algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise CREDENTIALS_EXCEPTION
    except JWTError:
        raise CREDENTIALS_EXCEPTION
    user = await get_user_by_email(db, email)
    if user is None:
        raise CREDENTIALS_EXCEPTION
    return user


