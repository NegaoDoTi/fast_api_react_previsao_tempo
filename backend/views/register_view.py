from controllers.register_controller import RegisterController
from schemas.message_schemas import ErrorMessage
from schemas.user_schemas import UserCreatedResponse
from fastapi.responses import JSONResponse
from fastapi import status

class RegisterView:
    def __init__(self):
        self.__controller = RegisterController()
        
    async def handle_register_user(self, username: str, email: str, password:str) -> dict[str, str]:
        result = await self.__controller.register_user(username, email, password)
        
        if isinstance(result, dict):
            return JSONResponse(ErrorMessage(message=result["message"]).dict(), status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        return UserCreatedResponse(username=username, email=email, password=password)