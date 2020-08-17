import os
import json
import math
from more_itertools import chunked
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape


def read_books():
    with open('books.json', 'r') as file:
        books_json = json.load(file)
        return books_json


def on_reload():
    pages_folder = 'pages'
    os.makedirs(pages_folder, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    books = read_books()
    pages = range(1, math.ceil(len(books) / 20) + 1)
    filename = 'index.html'
    for books_group_number, books_group in enumerate(chunked(books, 20), start=1):
        rendered_page = template.render(
            pages=pages,
            books=books_group,
            current_page=books_group_number
        )
        if books_group_number > 1:
            filename = os.path.join(pages_folder, f'index{books_group_number}.html')
        with open(filename, 'w', encoding="utf8") as file:
            file.write(rendered_page)


def main():
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')


if __name__ == "__main__":
    main()
