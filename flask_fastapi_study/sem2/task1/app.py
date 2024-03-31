"""
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/task1', methods=['GET', 'POST'])
def submit():
    match request.method:
        case 'GET':
            return render_template('index.html')
        case 'POST':
            return render_template('task1.html', name=request.form.get('name'))


if __name__ == '__main__':
    app.run()
