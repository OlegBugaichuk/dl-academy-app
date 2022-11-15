from pydantic import EmailStr

from .auth_helpers import get_hash


async def signup_confirm_email_send(email: EmailStr):
    hashed_email = get_hash(email)
    print(hashed_email)
