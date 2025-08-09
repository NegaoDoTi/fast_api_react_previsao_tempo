from httpx import AsyncClient
from config.env import API_KEY_TEMPO
from zoneinfo import ZoneInfo
from datetime import datetime

class WeatherService:
    async def get_lat_lon_city(self, name: str) -> dict[float, float]:
        
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={name}&Limit=1&appid={API_KEY_TEMPO}"
        
        header = {
            "Content-Type" : "application/json"
        }
        
        async with AsyncClient() as client:
            result = await client.get(url=url, headers=header)
            
        if result.status_code != 200 and result.status_code != 201:
            raise Exception(f"Erro ao consultar API de Geolocalização, tente novamente mais tarde!")
        
        raw = result.json()
        
        if len(raw) ==  0:
            raise Exception(f"Cidade {name} não encontrada, na API de Geolocalização")
        
        data = {
            "lat" : raw[0]["lat"],
            "lon" : raw[0]["lon"]
        }
        
        return data
    
    async def get_city_weathe_data(self, name:str, state:str, lat:float, lon:float) -> dict:
        
        now = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%d/%m/%Y : %H:%M")
        
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=pt_br&units=metric&appid={API_KEY_TEMPO}"
        
        header = {
            "Content-Type" : "application/json"
        }
        
        async with AsyncClient() as client:
            result =  await client.get(url=url, headers=header)
            
        if result.status_code != 200 and result.status_code != 201:
            raise Exception("Erro ao consultar API de clima tente novamente mais tarde!")
        
        raw = result.json()
        
        data = {
            "cidade" : name,
            "estado" : state,
            "latitude" : lat,
            "lon" : lon,
            "ceu" : raw["weather"][0]["description"],
            "temperatura" : f'{raw["main"]["temp"]}ºC',
            "temperatura_min" : f'{raw["main"]["temp_min"]}ºC',
            "temperatura_max" : f'{raw["main"]["temp_max"]}ºC',
            "humidade_ar" : f'{raw["main"]["humidity"]}%',
            "velocidade_vento" : f'{raw["wind"]["speed"]} Metros/Segundos'
        }
        
        return data