from services.users_service import UserService
from traceback import format_exc
from sqlalchemy.exc import IntegrityError
from auth.auth_handler import generate_password_hash

class RegisterController:
    
    def __init__(self):
        self.users_service = UserService()
        
    async def register_user(self, username:str, email:str, password:str):
        try:
            hash_password = generate_password_hash(password)
            
            await self.users_service.create_user(username, email, hash_password)
        except IntegrityError as e:
            return {"message" : f"Erro ao criar usuario o campo: {e.orig} já foi cadastrado"}
        except Exception:
            print(format_exc())
            return {"message" : "Inesperado ao criar usuario tente novamente mais tarde"}
        
        return True