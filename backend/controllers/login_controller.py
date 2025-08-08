from services.users_service import UserService
from auth.auth_handler import verify_password, generate_access_token
from traceback import format_exc

class LoginController:
    def __init__(self):
        self.users_service = UserService()
        
    async def login_user(self, email:str, password:str) -> dict:
        try:
            user = await self.users_service.find_user(email)
            
            if not user:
                return {"message" : "Usuario não existe"}
            
            if not verify_password(password, user.password):
                return {"message": "Senha incorreta!"}
            
            return generate_access_token({"user_id" : str(user.id), "user_email" : user.email})
            
        except Exception:
            print(format_exc())
            return {"message" : "Erro inesperado ao cadastrar usuario. Contate o ADM!"}