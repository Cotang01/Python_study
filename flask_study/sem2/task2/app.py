"""
Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""
from pathlib import PurePath, Path

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.get('/task1')
def submit_get():
    return render_template('index.html')


@app.post('/task1')
def submit_post():
    return render_template('task1.html', name=request.form.get('name'))


@app.get('/task2')
def upload_get():
    return render_template('task2.html')


@app.post('/task2')
def upload_post():
    file = request.files.get('file')
    file_name = secure_filename(file.filename)
    file.save(PurePath.joinpath(Path.cwd(), 'static', 'uploads',
                                file_name))
    return f"Файл {file_name} загружен на сервер"


if __name__ == '__main__':
    app.run()
