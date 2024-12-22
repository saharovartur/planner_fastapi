from hmac import compare_digest

from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSingIn

user_router = APIRouter(tags=['User'])

users = {}


@user_router.post('/signup')
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Пользователь с такой почтой уже есть')
    if len(data.password) < 10:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Пароль должен содержать не менее 10 символов")

    users[data.email] = data
    return {
        "message": 'Пользователь успешно зарегистрирован!'
    }


@user_router.post('/signin')
async def sign_user_in(user: UserSingIn) -> dict:
    if user.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Такой пользователь не зарегистрирован')

    # Используем compare_digest для безопасного сравнения паролей
    if not compare_digest(users[user.email].password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Переданы неверные учетные данные')

    return {
        "message": "Пользователь успешно вошел в систему"
    }
