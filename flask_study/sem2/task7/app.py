"""
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
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


@app.get('/task5')
def calculate_get():
    return render_template('task5.html')


@app.post('/task5')
def calculate_post():
    num1 = int(request.form.get('num1'))
    num2 = int(request.form.get('num2'))
    oper = request.form.get('operations')
    result = 0
    print(oper)
    match oper:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                flash('You cannot divide by zero!', 'error')
                return redirect('task5')
            result = num1 / num2
    return render_template('task5_result.html', result=result)


@app.get('/task6')
def verify_get():
    return render_template('task6.html')


@app.post('/task6')
def verify_post():
    age_threshold = 18
    name = request.form.get('name')
    age = int(request.form.get('age'))
    if age < age_threshold:
        flash('You have to be over 18 years old', 'error')
        return redirect('task6')
    return render_template('task6_access.html', name=name)


@app.get('/task7')
def get_square_get():
    return render_template('task7.html')


@app.post('/task7')
def get_square_post():
    num = int(request.form.get('num1'))
    sq_num = num ** 2
    return render_template('task7_result.html', number=num, squared=sq_num)


if __name__ == '__main__':
    app.run()
