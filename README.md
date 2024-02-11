Клонируем репозиторий git clone https://github.com/nishealsohuwe/django_RestAPI.git
Переходим в папку с проектом cd base
Устанавливаем виртуальное окружение python -m venv env
Запускаем виртуальное окружение source env/Scripts/activate
Устанавливаем в виртуальном окружении зависимости для проекта python -m pip install --no-cache-dir -r requirements.txt
Делаем миграции для создания базы данных python manage.py makemigrations && python manage.py migrate
Запускаем локальный сервер python manage.py runserver
По адресу http://localhost:8000 будет доступен список записей о gjkmpjdfntkz[, a по адресу http://localhost:8000/api/users та же информация через API.
