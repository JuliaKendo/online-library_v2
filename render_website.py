import json
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape


def read_books():
    with open('books.json', 'r') as file:
        books_json = json.load(file)
        return books_json


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        books=read_books()
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')


if __name__ == "__main__":
    main()
