from services.cities_service import CitiesService
from services.weather_service import WeatherService
from traceback import format_exc

class CitiesController:
    def __init__(self):
        self.cities_service = CitiesService()
        self.weather_service = WeatherService()
    
    async def get_all_cities(self, user_id:str) -> list[dict]:
        cities = await self.cities_service.get_all_cities(user_id)
        
        data = []
        try:
            for city in cities:
                result = await self.weather_service.get_city_weathe_data(
                    city.name,
                    city.state,
                    city.lat,
                    city.lon
                )
                
                data.append(result)
        except Exception:
            return {"message" : f"Erro ao consultar a cidade {city.name}"}
            
        return data
    
    async def register_new_city(self, name:str, state:str, user_id:str):
        
        try:
            result = await self.weather_service.get_lat_lon_city(name)
        except Exception as e:
            return {"message" : f"{e}"}
        
        try:        
            await self.cities_service.create_city(user_id, name, state, result["lat"], result["lon"])
        except Exception:
            print(format_exc())
            return {"message" : f"Erro ao cadatrar cidae"}
        
        return result