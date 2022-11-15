from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.users import (get_user_by_email, get_user_by_id, get_users_list,
                            signup_user)
from src.crud.courses import get_user_courses
from src.schemas.users import SignIn, SignUp, Token, UserBase, User
from src.schemas.courses import Course
from src.db.depends import get_db

from .auth_helpers import create_access_token, verify_hash
from .email_services import signup_confirm_email_send
from .depends import get_current_user


users_router = APIRouter(prefix='/users')


@users_router.get('/', response_model=list[UserBase])
async def users_list(db: AsyncSession = Depends(get_db)) -> list[UserBase]:
    return await get_users_list(db)


@users_router.get('/me', response_model=UserBase)
async def current_user_profile(current_user: User = Depends(get_current_user)
                               ) -> UserBase:
    return current_user


@users_router.get('/{id}', response_model=UserBase)
async def user_detail(id: int, db: AsyncSession = Depends(get_db)) -> UserBase:
    user = await get_user_by_id(db, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User not found')
    return user


@users_router.get('/{id}/courses', response_model=list[Course])
async def user_courses(id: int,
                       db: AsyncSession = Depends(get_db)) -> list[Course]:
    courses = await get_user_courses(db, id)
    return courses


@users_router.post('/signup')
async def signup(email: str = Form(),
                 password: str = Form(),
                 confirm_password: str = Form(),
                 db: AsyncSession = Depends(get_db)):

    data = SignUp(email=email,
                  password=password,
                  confirm_password=confirm_password)
    await signup_user(db, data)
    await signup_confirm_email_send(data.email)
    return {'message': 'Confirm email'}


@users_router.post('/signin', response_model=Token)
async def signin(email: str = Form(),
                 password: str = Form(),
                 confirmation_code: str = '',
                 db: AsyncSession = Depends(get_db)):

    data = SignIn(email=email, password=password)
    user = await get_user_by_email(db, data.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Login Error')

    if not verify_hash(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Login Error')

    if user.active or (confirmation_code and verify_hash(data.email,
                                                         confirmation_code)):
        if not user.active:
            user.active = True

        access_token = create_access_token(user.email)
        return Token(token=access_token)

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail='Code error')
