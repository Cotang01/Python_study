"""
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст.
"""
import datetime

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


@app.route('/news')
def news():
    news_data = [{'article': 'article1',
                  'description': 'description1',
                  'publish_time': datetime.datetime.now()},
                 {'article': 'article2',
                  'description': 'description2',
                  'publish_time': datetime.datetime.now()}
                 ]
    return render_template('news.html', news=news_data)


if __name__ == '__main__':
    app.run()

