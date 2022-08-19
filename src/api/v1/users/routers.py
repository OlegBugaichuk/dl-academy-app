from fastapi import APIRouter, Depends, HTTPException, status
from src.crud.users import get_user_by_email, get_user_by_id, get_users_list
from src.schemas.users import SignIn, SignUp, Token, UserBase, User

from .auth_helpers import create_access_token, verify_hash
from .email_services import signup_confirm_email_send
from .depends import get_current_user

users_router = APIRouter(prefix='/users')


@users_router.get('/', response_model=list[UserBase])
async def users_list() -> list[UserBase]:
    return await get_users_list()


@users_router.get('/me', response_model=UserBase)
async def user_detail(current_user: User = Depends(get_current_user)) -> UserBase:
    return current_user.dict()


@users_router.get('/{id}', response_model=UserBase)
async def user_detail(id: int) -> UserBase:
    user = await get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User not found')
    return user


@users_router.post('/signup')
async def signup(data: SignUp = Depends()):
    await signup_confirm_email_send(data.email)
    return {'message': 'Confirm email'}


@users_router.post('/signin', response_model=Token)
async def signin(data: SignIn = Depends(), confirmation_code: str = ''):
    user = await get_user_by_email(data.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Login Error')

    if not verify_hash(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Login Error')

    
    if user.active or (confirmation_code and verify_hash(data.email,
                                                         confirmation_code)):
        if not user.active:
            user.active = True

        access_token = create_access_token({"sub": user.email})
        return Token(token=access_token)

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail=f'Code error')
