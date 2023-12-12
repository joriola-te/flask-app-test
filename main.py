from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_bold():
        return f"<b>{function()}</b>"

    return wrapper_bold


def make_italic(function):
    def wrapper_italic():
        return f"<em>{function()}</em>"

    return wrapper_italic


def make_underline(function):
    def wrapper_underline():
        return f"<u>{function()}</u>"

    return wrapper_underline


@app.route('/')
@make_bold
# @make_italic
@make_underline
def home():
    return '<h1>Hello, World!<h1>'


@app.route('/<path:name>')
def about(name):
    return f"<h1>This is the {name} page.<h1>"


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
