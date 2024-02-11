Запускаем проект на своей машине:

1.Клонируем репозиторий git clone https://github.com/nishealsohuwe/django_RestAPI.git

2.Переходим в папку с проектом cd base

3.Устанавливаем виртуальное окружение python -m venv env

4.Запускаем виртуальное окружение source env/Scripts/activate

5.Устанавливаем в виртуальном окружении зависимости для проекта python -m pip install --no-cache-dir -r requirements.txt

6.Делаем миграции для создания базы данных python manage.py makemigrations && python manage.py migrate

7.Запускаем локальный сервер python manage.py runserver

8.По адресу http://localhost:8000 будет доступен список записей о gjkmpjdfntkz[, a по адресу http://localhost:8000/api/users та же информация через API.
