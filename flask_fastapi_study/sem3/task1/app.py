"""
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.
"""
import random

from flask import Flask, render_template
from models import db, Student, Faculty

app = Flask(__name__)

app.config.from_object('config')
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.drop_all()
    db.create_all()
    print('created tables')


@app.cli.command('fill-db')
def fill_db():
    faculties = ['Юридический', 'Математический', 'Технический']
    for f in faculties:
        faculty = Faculty(name=f)
        db.session.add(faculty)
    db.session.commit()
    print('Faculties filled')

    for student in range(1, 10):
        toss = random.randint(0, 1)
        fname = f'fname{student}'
        sname = f'sname{student}'
        age = random.randint(18, 40)
        gender = 'M' if toss else 'F'
        group = f'group{random.randint(1, 3)}'
        faculty_id = random.randint(1, 3)
        student = Student(fname=fname, sname=sname, age=age, gender=gender,
                          group=group, faculty_id=faculty_id)
        db.session.add(student)
    db.session.commit()
    print('Students filled')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/show_students')
def show_students():
    students = Student.query.all()
    return render_template('students.html', students=students)


@app.route('/show_faculties')
def show_faculties():
    faculties = Faculty.query.all()
    return render_template('faculties.html', faculties=faculties)


if __name__ == '__main__':
    app.run()
