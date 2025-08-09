from fastapi import APIRouter, Depends, Form
from schemas.user_schemas import UserCreatedResponse, UserRegisterForm
from views.register_view import RegisterView
from fastapi.responses import JSONResponse

register_route = APIRouter()

@register_route.post("/register")
async def register_user(form_data: UserRegisterForm = Depends(UserRegisterForm.form)):
    return await RegisterView().handle_register_user(form_data.username, form_data.email, form_data.password)