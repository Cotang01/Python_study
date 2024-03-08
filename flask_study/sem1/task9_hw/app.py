"""
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.
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


products_list = ['hat', 'shoes']


@app.route('/products')
def products():
    return render_template('products.html', products=products_list)


@app.route('/products/<product>')
def concrete_product(product):
    return render_template(f'{product}.html')


if __name__ == '__main__':
    app.run()
