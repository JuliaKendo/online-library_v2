import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def read_books():
    with open('books.json', 'r') as file:
        books_json = json.load(file)
        return books_json


def main():
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

    server = HTTPServer(('localhost', 5500), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
