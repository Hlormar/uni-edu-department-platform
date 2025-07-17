не 🥺 коммитить 🥰 в m-mastew без 👉👈 о-обсуждения (●'◡'●)*happy sigh*

БД на текущий момент не настоящая, а захардкоженные словари!!!

Готово:
  Фронт:
    login.html
    dashboard.html
  Бэк:
    auth.py

Установка и запуск:

**Linux**:
`python -m venv venv`
`source venv/bin/activate
`pip install -r requirements.txt`


Запустите бэкэенд
`cd backend`
`uvicorn main:app --reload`

Запустите фронтэнд в другом терминале:
`cd frontend`
`python -m http.server 8001`

Откройте в браузере:
http://localhost:8001/login.html
