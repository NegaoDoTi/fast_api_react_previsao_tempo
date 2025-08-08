from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

def verify_password(password:str, hash_password:str):
    return pwd_context.verify(password, hash_password)

def generate_password_hash(password:str) -> str:
    return pwd_context.hash(password)