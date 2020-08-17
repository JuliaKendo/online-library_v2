# Онлайн библиотека

[Сайт онлайн библиотеки](https://juliakendo.github.io/online-library_v2/pages/index.html), созданный на базе парсинга книг с сайта [http://tululu.org](http://tululu.org). 

![Demo library](demo_lib.gif)

## Установка

Python3 должен быть установлен. Используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

Загрузить необходимые для заполнения сайта данные с [http://tululu.org](http://tululu.org) с помошью  [парсера книг](https://github.com/JuliaKendo/online-library). Скаченные книги положить в папку `books`, изображения - в папку `images`, *.json файл с результатами парсинга - в корень скрипта, либо в любую папку, указав ее в параметрах коммандной строки.
Переменные в данном скрипте заполнять не требуется.

## Запуск

Запускают скрипт с необязательным параметром:
    1. ```-j JSON_PATH, --json_path```        Путь к *.json файлу с результатами парсинга [http://tululu.org](http://tululu.org), по умолчанию `books.json`

```
python.exe render_website.py -j books.json
```	

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
