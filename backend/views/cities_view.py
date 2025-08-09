from fastapi import Request, status
from fastapi.responses import JSONResponse
from schemas.city_schemas import CityRegisterResponse
from validators.verify_login import verify_login_jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from controllers.cities_controller import CitiesController

class CitiesView:
    def __init__(self):
        self.__controller = CitiesController()
        
    async def get_all_cities(self, request: Request) -> JSONResponse:
        try:
            token = request.headers["Authorization"].split("Bearer ")[-1]
        except Exception:
            return JSONResponse({"message" : "Token de autorização deve ser fornecido!"}, status.HTTP_401_UNAUTHORIZED)
        
        try:
            payload = await verify_login_jwt(token)
        except ExpiredSignatureError:
            return JSONResponse({"message" : "Token expirado faça login novamente!"}, status.HTTP_401_UNAUTHORIZED)
        except InvalidTokenError:
            return JSONResponse({"message" : "Token invalido!"}, status.HTTP_401_UNAUTHORIZED)
        
        cities_data = await self.__controller.get_all_cities(payload["user_id"])
        
        if "message" in cities_data:
            return JSONResponse(cities_data, status.HTTP_403_FORBIDDEN)
        
        return JSONResponse(cities_data, status.HTTP_200_OK)
        
    async def register_new_city(self, name:str, state:str, request: Request) -> JSONResponse | CityRegisterResponse:
        try:
            token = request.headers["Authorization"].split("Bearer ")[-1]
        except Exception:
            return JSONResponse({"message" : "Token de autorização deve ser fornecido!"}, status.HTTP_401_UNAUTHORIZED)
        
        try:
            payload = await verify_login_jwt(token)
        except ExpiredSignatureError:
            return JSONResponse({"message" : "Token expirado faça login novamente!"}, status.HTTP_401_UNAUTHORIZED)
        except InvalidTokenError:
            return JSONResponse({"message" : "Token invalido!"}, status.HTTP_401_UNAUTHORIZED)
        
        user_id = payload["user_id"]
        
        if len(state) > 2:
            return JSONResponse({"message" : "Sigla do estado incorreta!"}, status.HTTP_400_BAD_REQUEST)
        
        state = str(state.upper())
        
        result = await self.__controller.register_new_city(name, state, user_id)
        
        if isinstance(result, dict) and "message" in result:
            code = status.HTTP_500_INTERNAL_SERVER_ERROR
            
            return JSONResponse(result, code)
        
        return CityRegisterResponse(name=name, state=state, lat=result["lat"], lon=result["lon"])
            
        