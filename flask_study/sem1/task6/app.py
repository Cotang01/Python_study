"""
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
"""
from flask import Flask, render_template

app = Flask(__name__)

data_students = [{'fname': 'Иван',
                  'lname': 'Петров',
                  'age': 19,
                  'avg_score': 4},
                 {'fname': 'Оля',
                  'lname': 'Петрова',
                  'age': 20,
                  'avg_score': 5}]


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/students')
def students():
    return render_template('students.html', students=data_students)


if __name__ == '__main__':
    app.run()

