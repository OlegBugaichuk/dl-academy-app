from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hash(raw_string: str) -> str:
    return pwd_context.hash(raw_string)


def verify_hash(raw_string: str, hash: str) -> bool:
    return pwd_context.verify(raw_string, hash)