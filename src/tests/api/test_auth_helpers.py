from jose import jwt
from passlib.context import CryptContext
from src.core.settings import settings
from src.api.v1.users.auth_helpers import (get_hash, verify_hash,
                                           create_access_token)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
TEST_RAW_STRING = 'test'


def test_get_hash():
    test_hash = get_hash(TEST_RAW_STRING)
    assert pwd_context.verify(TEST_RAW_STRING, test_hash)


def test_verify_hash():
    test_hash = pwd_context.hash(TEST_RAW_STRING)
    assert verify_hash(TEST_RAW_STRING, test_hash) is True

    invalid_test_raw_string = 'invalid_test'
    assert verify_hash(invalid_test_raw_string, test_hash) is False


def test_create_access_token():
    test_user_email = 'test@test.com'
    access_token = create_access_token(test_user_email)
    token_data = jwt.decode(access_token,
                            settings.secret_key,
                            algorithms=[settings.hash_algorithm])

    assert token_data.get('sub') == test_user_email
    assert token_data.get('exp') is not None
