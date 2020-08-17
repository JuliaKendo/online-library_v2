# Онлайн библиотека

Сайт онлайн библиотеки, созданный на базе парсинга книг с сайта [http://tululu.org](http://tululu.org). 

![Demo library](demo_lib.gif)

## Установка

Python3 должен быть установлен. Используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

Получить необходимые для заполнения сайта данные с [http://tululu.org](http://tululu.org). Выполняется при помощи [парсера книг с http://tululu.org](https://github.com/JuliaKendo/online-library).
Переменные окружения отсутствуют.

## Запуск

Запускают скрипт с необязательным параметром:
    1. ```-j JSON_PATH, --json_path```        Путь к *.json файлу с результатами парсинга [http://tululu.org](http://tululu.org), по умолчанию `books.json`

```
python.exe render_website.py -j books.json
```	

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
