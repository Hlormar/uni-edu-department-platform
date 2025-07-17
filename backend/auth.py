from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status

from db import fake_users_db, pwd_context

# Настройки
SECRET_KEY = "campus2028" # Секретный ключ для подписи JWT-токенов
ALGORITHM = "HS256" # Шифрование токенов
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Объект для хэширования паролей
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Указывает, что токен запрашивается по /token


# Модель для логина = данные, которые отправляются при нажатии "Войти"
class UserLogin(BaseModel):
    username: str
    password: str

# Модель токена
class Token(BaseModel):
    access_token: str
    token_type: str

# Проверка пароля
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Получение пользователя
def get_user(username: str):
    return fake_users_db.get(username)

# Аутентификация
# Существует ли пользователь?
# Совпадает ли хеш пароля?
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user


# Генерация токена
# Формат данных:
#    id              Int
#    role-id         Int
#    email           Str
#    fio             Str
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

