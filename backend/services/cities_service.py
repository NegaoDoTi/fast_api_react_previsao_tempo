from database.connection import async_session
from models.Cities import Cities
from sqlalchemy.future import select


class CitiesService:
    async def create_city(self, user_id:str, name:str, state:str, lat:float, lon:float) -> None:
        async with async_session() as session:
            city = Cities(user_id, name, state, lat, lon)
            
            session.add(city)
            await session.commit()
    
    async def get_all_cities(self, user_id:str) -> list[Cities]:
        async with async_session() as session:
            query = select(Cities).where(Cities.user_id == user_id)
            
            result = await session.execute(query)
            
            cities = result.scalars().all()
            
        return cities