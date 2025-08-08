from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user_schemas import UserToken
from views.login_view import LoginView

login_route = APIRouter()

@login_route.post("/login")
async def login_user(form_data : OAuth2PasswordRequestForm = Depends()) -> UserToken:
    return await LoginView().login_user(form_data.username, form_data.password)