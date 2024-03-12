"""
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""
import secrets
import logging
from pathlib import PurePath, Path
from flask import Flask, request, render_template, redirect, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = secrets.token_hex()
logger = logging.getLogger(__name__)


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


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Page not found',
        'url': request.base_url
    }
    return render_template('404.html', context=context)


@app.get('/task3')
def login_get():
    return render_template('task3.html')


@app.post('/task3')
def login_post():
    cor_lgn = 'admin'
    cor_pswd = 'admin'
    login_ = request.form.get('user-login')
    password_ = request.form.get('user-password')
    if cor_lgn == login_ and cor_pswd == password_:
        return render_template('task3_greet.html', name=cor_lgn)
    flash('Wrong login or password!', 'error')
    return redirect('task3')


@app.get('/task4')
def count_words_get():
    return render_template('task4.html')


@app.post('/task4')
def count_words_post():
    counter = len(request.form.get('user-text').split())
    return render_template('task4_count.html', counter=counter)


if __name__ == '__main__':
    app.run()
