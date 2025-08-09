from controllers.register_controller import RegisterController
from schemas.user_schemas import UserCreatedResponse
from fastapi.responses import JSONResponse
from fastapi import status

class RegisterView:
    def __init__(self):
        self.__controller = RegisterController()
        
    async def handle_register_user(self, username: str, email: str, password:str) -> JSONResponse | UserCreatedResponse:
        result = await self.__controller.register_user(username, email, password)
        
        if isinstance(result, dict):
            code = status.HTTP_400_BAD_REQUEST
            
            if "inesperado" in result["message"]:
                code = status.HTTP_500_INTERNAL_SERVER_ERROR
            
            
            return JSONResponse(result, code)
        
        return UserCreatedResponse(username=username, email=email, password=password)