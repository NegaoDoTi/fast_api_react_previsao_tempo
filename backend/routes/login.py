from fastapi import APIRouter, Depends
from schemas.user_schemas import UserToken
from views.login_view import LoginView
from schemas.user_schemas import UserLoginForm

login_route = APIRouter()

@login_route.post("/login")
async def login_user(form_data : UserLoginForm = Depends(UserLoginForm.form)) -> UserToken:
    return await LoginView().login_user(form_data.email, form_data.password)