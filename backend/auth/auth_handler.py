from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from config.env import SECRECT_KEY, ALGORITHM
import jwt

pwd_context = CryptContext(schemes=["bcrypt"])

def verify_password(password:str, hash_password:str):
    return pwd_context.verify(password, hash_password)

def generate_password_hash(password:str) -> str:
    return pwd_context.hash(password)

def generate_access_token(data : dict, expires_time: timedelta = timedelta(hours=1)) -> str:
    encode_data = data.copy()
    
    expire = datetime.now() + expires_time
    
    encode_data.update({"expire" : expire.strftime("%d/%m/%Y %H:%M:%S")})
    
    encode_jwt = jwt.encode(encode_data, SECRECT_KEY, ALGORITHM)
    
    return encode_jwt