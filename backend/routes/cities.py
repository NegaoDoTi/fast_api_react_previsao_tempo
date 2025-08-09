from fastapi import APIRouter, Request
from views.cities_view import CitiesView
from schemas.city_schemas import CityRegister, CityRegisterResponse
from fastapi.responses import JSONResponse
cities_route = APIRouter()


@cities_route.get("/cities")
async def get_all_cities(request: Request):
    return await CitiesView().get_all_cities(request)

@cities_route.post("/cities")
async def register_city(city: CityRegister, request: Request):
    return await CitiesView().register_new_city(city.name, city.state, request)