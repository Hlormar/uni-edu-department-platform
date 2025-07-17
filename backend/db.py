from passlib.context import CryptContext # Для безопасного хранения паролей

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Объект для хэширования паролей


# Пример пользователя в БД (в реальности — из SQLite)
#email:
#    email,
#    id,
#    password-,
#    role,
#    fio
fake_users_db = {
    "university-worker@stud.ru": {
        "email": "university-worker@stud.ru",
        "id": "1",
        "password": pwd_context.hash("123"),
        "role": "1", # 1 = university, взято из roles БД
        "fio": "Котаро Амон"
    },
    "department-worker@gov.ru": {
        "email": "department-worker@gov.ru",
        "id": "2",
        "password": pwd_context.hash("456"),
        "role": "2", # 2 = department, взято из roles БД
        "fio": "Акира Мадо"
    }
}

