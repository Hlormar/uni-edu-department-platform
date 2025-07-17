from passlib.context import CryptContext # Для безопасного хранения паролей

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Объект для хэширования паролей

fake_roles_db={
    "1": "department",
    "2": "ТюмГу",
}

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
        "id": "2",
        "password": pwd_context.hash("123"),
        "role": "2", # 2 = university, взято из roles БД
        "fio": "Котаро Амон"
    },
    "department-worker@gov.ru": {
        "email": "department-worker@gov.ru",
        "id": "1",
        "password": pwd_context.hash("456"),
        "role": "1", # 1 = department, взято из roles БД
        "fio": "Акира Мадо"
    }
}

#id integer
#template str
#university str
#last_updated String
#creation_date string
#updated_by String
#file str
fake_tables_db = {
    "1":{
        "template": "Количество обучающихся из числа лиц-участников СВО",
        "university": "ТюмГУ",
        "university-id": "2",
        "last_updated": "16:00 17.07.2025",
        "creation_date": "13:20 11.07.2025",
        "updated_by": "Иван Иванов Иванович",
        "file": "Template1-Тюмгу.xlsx"
        },
    "2":{
        "template": "Количество обучающихся из числа лиц-участников СВО",
        "university": "ТИУ",
        "university-id": "3",
        "last_updated": "12:03 16.07.2025",
        "creation_date": "13:20 11.07.2025",
        "updated_by": "Вячеслав Плесовских Александрович",
        "file": "Template1-ТИУ.xlsx"
         },
    "3":{
        "template": "Количество обучающихся из числа лиц-участников СВО",
        "university": "ТюмГМУ",
        "university-id": "4",
        "last_updated": "11:00 17.07.2025",
        "creation_date": "13:20 11.07.2025",
        "updated_by": "Михаил Зиминев Константинович",
        "file": "Template1-ТюмГМУ.xlsx"
        },
    "4":{
        "template": "Количество обучающихся из числа лиц-участников СВО",
        "university": "ТГИК",
        "university-id": "5",
        "last_updated": "14:50 17.07.2025",
        "creation_date": "13:20 11.07.2025",
        "updated_by": "Сон Ки хун",
        "file": "Template1-ТГИК.xlsx"
        },
    "5":{
        "template": "Количество обучающихся из числа лиц-участников СВО",
        "university": "ГАУСЗ",
        "university-id": "6",
        "last_updated": "13:22 15.07.2025",
        "creation_date": "13:20 11.07.2025",
        "updated_by": "Иван Иванов Иванович",
        "file": "Template1-ГАУСЗ.xlsx"
        },
}
