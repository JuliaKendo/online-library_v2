import os
import json
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
    for books_group_number, books_group in enumerate(chunked(books, 20)):
        rendered_page = template.render(books=books_group)
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
