import os
import json
import math
import argparse
from dotenv import load_dotenv
from more_itertools import chunked
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape


def create_parser():
    parser = argparse.ArgumentParser(description='Параметры запуска скрипта')
    parser.add_argument('-j', '--json_path', default='books.json', help='Путь к *.json файлу с результатами')
    return parser


def read_books(filename):
    with open(filename, 'r') as file:
        books_json = json.load(file)
        return books_json


def on_reload(json_path):
    pages_folder = 'pages'
    os.makedirs(pages_folder, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    books = read_books(json_path)
    pages = range(0, math.ceil(len(books) / 20))
    for books_group_number, books_group in enumerate(chunked(books, 20)):
        rendered_page = template.render(
            pages=pages,
            books=books_group,
            current_page=books_group_number
        )
        filename = os.path.join(pages_folder, f'index{books_group_number if books_group_number > 0 else ""}.html')
        with open(filename, 'w', encoding="utf8") as file:
            file.write(rendered_page)


def main():
    load_dotenv()
    parser = create_parser()
    args = parser.parse_args()
    server_ip = os.getenv('SERVER_IP')
    server_port = os.getenv('SERVER_PORT')

    try:

        on_reload(args.json_path)
        server = Server()
        server.watch('template.html', on_reload(args.json_path))
        server.serve(root='.', host=server_ip, port=server_port)

    except OSError as error:
        print(f'Системная ошибка чтения, записи: {error}')

    except (KeyError, ValueError, TypeError) as error:
        print(f'Ошибка обновления данных сайта: {error}')


if __name__ == "__main__":
    main()
