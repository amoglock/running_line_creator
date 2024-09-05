<h1 align="center">Проект для создания видео бегущей строки</h1>
<p align="center">
<img src="https://img.shields.io/badge/python-3.12-blue?logo=python">
<img src="https://img.shields.io/badge/django-green?logo=django">
<img src="https://img.shields.io/badge/OpenCV-Python-red">
</p>

Проект создает короткие видео (3 секунды) в виде бегущей строки из текста введенного пользователем.
Формат видео *.mp4.
Готовые файлы хранятся в {папка проекта}/uploads/media.
Пользователь может загрузить видео через браузер в "загрузки".

### Запуск приложения
Клонировать репозиторий:
```commandline
git clone https://github.com/amoglock/running_line_creator
```

Открыть репозиторий в IDE или терминале.<br>
Активировать виртуальное окружение.<br>
Установить зависимости из requirements.txt
```commandline
pip install -r requirements.txt
```
Выполнить миграцию БД:
```commandline
python manage.py makemigrations
python manage.py migrate
```

Запустить сервер Django:
```commandline
python manage.py runserver
```
После запуска сервера, приложение доступно по адресу http://127.0.0.1:8000/main (для Linux)