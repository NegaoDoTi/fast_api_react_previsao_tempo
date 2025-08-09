from database.connection import async_session
from models.Users import Users
from uuid import uuid4
from sqlalchemy.future import select

class UserService:
    async def create_user(self, username: str, email:str, hash_password:str) -> None:
        async with async_session() as session:
            id = str(uuid4())
            
            session.add(Users(id, username, email, hash_password))
            await session.commit()
            
        return
            
    async def find_user(self, email:str):
        async with async_session() as session:
            query = select(Users).where(Users.email == email)
            result = await session.execute(query)
            
            user = result.scalars().one()
            
        return user