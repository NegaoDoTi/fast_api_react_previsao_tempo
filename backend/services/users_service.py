from database.connection import async_session
from models.Users import Users
from uuid import uuid4

class UserService:
    async def create_user(self, username: str, email:str, hash_password:str):
        async with async_session() as session:
            id = str(uuid4())
            
            session.add(Users(id, username, email, hash_password))
            await session.commit()
            