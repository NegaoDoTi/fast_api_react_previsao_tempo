from passlib.context import CryptContext
from datetime import datetime, timedelta
from config.env import SECRECT_KEY, ALGORITHM
import jwt
from zoneinfo import ZoneInfo

pwd_context = CryptContext(schemes=["bcrypt"])

def verify_password(password:str, hash_password:str):
    return pwd_context.verify(password, hash_password)

def generate_password_hash(password:str) -> str:
    return pwd_context.hash(password)

def generate_access_token(data : dict, expires_time: timedelta = timedelta(hours=1)) -> str:
    encode_data = data.copy()
    
    now = datetime.now(ZoneInfo("America/Sao_Paulo"))
    expire = now + expires_time
        
    encode_data.update({"iat" : now})
    
    encode_data.update({"exp" : expire})
    
    encode_jwt = jwt.encode(encode_data, SECRECT_KEY, ALGORITHM)
    
    return encode_jwt