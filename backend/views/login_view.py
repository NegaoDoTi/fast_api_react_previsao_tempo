from schemas.user_schemas import UserToken
from fastapi.responses import JSONResponse
from fastapi import status
from controllers.login_controller import LoginController

class LoginView:
    def __init__(self):
        self.__controller = LoginController() 
        
    async def login_user(self, email:str, password:str) ->  JSONResponse | UserToken:
        result = await self.__controller.login_user(email, password)
        
        if isinstance(result, dict):
            code = status.HTTP_200_OK
            
            if "inesperado" in result["message"]:
                code = status.HTTP_500_INTERNAL_SERVER_ERROR
            if "incorreta" in result["message"]:
                code = status.HTTP_401_UNAUTHORIZED
            if "não existe" in result["message"]:
                code = status.HTTP_400_BAD_REQUEST
                
            
            return JSONResponse(result, code)
        
        return UserToken(token=result, token_type="Bearer")