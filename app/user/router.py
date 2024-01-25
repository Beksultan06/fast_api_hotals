from fastapi import APIRouter, HTTPException
from app.user.dao import UsersDAO
from app.user.schemas import SUserRegister
from app.user.auth import get_password_hash


router = APIRouter(
    prefix="/auth",
    tags=["Auth  Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    # Проверка наличия пользователя с таким email
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        # Если пользователь уже существует, вернуть ошибку
        raise HTTPException(status_code=500)
    # Хеширование пароля
    hashed_password = get_password_hash(user_data.password)
    # Добавление нового пользователя
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
