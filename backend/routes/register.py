from fastapi import APIRouter, Depends, Form
from schemas.user_schemas import UserCreatedResponse, UserRegisterForm
from schemas.message_schemas import ErrorMessage
from views.register_view import RegisterView
from validators.users import valid_user
from typing import Annotated

register_route = APIRouter()


@register_route.post("/register", response_model=UserCreatedResponse | ErrorMessage )
async def register_user(form_data: UserRegisterForm = Depends(UserRegisterForm.form)):
    return await RegisterView().handle_register_user(form_data.username, form_data.email, form_data.password)