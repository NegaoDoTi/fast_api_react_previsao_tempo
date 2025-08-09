from jwt import decode
from config.env import SECRECT_KEY, ALGORITHM

async def verify_login_jwt(token:str) -> dict:
        decoded = decode(token, SECRECT_KEY, ALGORITHM)
        return decoded
    