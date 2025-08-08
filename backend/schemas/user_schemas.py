from pydantic import BaseModel, EmailStr
from fastapi import Form

class UserRegisterForm(BaseModel):
    username: str
    email: EmailStr
    password: str
    
    @classmethod
    def form(
        self,
        username: str = Form(...),
        email: EmailStr = Form(...),
        password: str = Form(...)
    ):
        return self(username=username, email=email, password=password)
    
class UserLoginForm(BaseModel):
    email: EmailStr
    password: str
    
    @classmethod
    def form(
        self,
        email: EmailStr = Form(...),
        password: str = Form(...)
    ):
        return self(email=email, password=password)
    
class UserCreatedResponse(BaseModel):
    username: str
    email: EmailStr
    
class UserToken(BaseModel):
    token: str
    token_type: str