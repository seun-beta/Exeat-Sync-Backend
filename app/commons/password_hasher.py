from argon2 import PasswordHasher

hasher = PasswordHasher()


def hash_password(password: str) -> str:
    return hasher.hash(password=password)


def verify_password(password: str, hashed_password: str) -> str:
    try:
        return hasher.verify(password=password, hash=hash_password)
    except:
        return False
