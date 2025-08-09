from pydantic import BaseModel
    
class CityRegister(BaseModel):
    name: str
    state: str
    
class CityRegisterResponse(BaseModel):
    name: str
    state: str
    lat: float
    lon: float