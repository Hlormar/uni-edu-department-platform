# backend/main.py

from fastapi import FastAPI, Depends, HTTPException, status
from auth import (
    authenticate_user,
    create_jwt_token,
    jwt,
    SECRET_KEY,
    ALGORITHM,
    Token,
    get_user,
    UserLogin,
    oauth2_scheme
)
#from fastapi.security import OAuth2PasswordBearer # Для работы с OAuth2 и JWT-токенами
#from pydantic import BaseModel # Для создания схем данных? (Pydantic)
#from passlib.context import CryptContext # Для безопасного хранения паролей
#from jose import jwt, JWTError # Для генерации и проверки JWT-токенов
#import sqlite3 # пока используется фейкова БД

app = FastAPI()

"""
# Настройки
SECRET_KEY = "campus2028" # Секретный ключ для подписи JWT-токенов
ALGORITHM = "HS256" # Шифрование токенов
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Объект для хэширования паролей
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Указывает, что токен запрашивается по /token



# Пример пользователя в БД (в реальности — из SQLite)
##email:
#   email,
#    id,
#    password-,
#    role,
#    fio
fake_users_db = {
    "university-worker@stud.ru": {
        "id": "1",
        "password": pwd_context.hash("123"),
        "role": "1", # 1 = university, взято из roles БД
        "fio": "Котаро Амон"
    },
    "department-worker@gov.ru": {
        "id": "2",
        "password": pwd_context.hash("456"),
        "role": "2", # 2 = department, взято из roles БД
        "fio": "Акира Мадо"
    }
}


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
def get_user(username: Str):
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
"""

# Роут для логина
@app.post("/token", response_model=Token)
async def login(login_data: UserLogin): # принимает переменную login_ типа  UserLogin
    user = authenticate_user(login_data.username, login_data.password) # Аутентификация

    if not user: # Кидает 401, если не успешно
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_data = {"id": user["id"], "email": user["email"], "role": user["role"], "fio": user["fio"]}
    access_token = create_jwt_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}



# Пример защищённого роута
#Этот маршрут требует токен. Он: 

#    Проверяет токен через Depends(oauth2_scheme)
#    Расшифровывает содержимое
#    Возвращает информацию о пользователе,
#    
#    чтобы:
#        Проверять, кто делает запрос
#        Разрешать доступ только авторизованным пользователям
#        Ограничивать доступ по ролям (например, только для департамента)


@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": f"Привет, {payload['fio']}, роль: {payload['role']}, email: {payload['email']}, id: {payload['id']}"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Неверный токен")
