"""
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email",
"Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе
данных, а пароль должен быть зашифрован.
"""
from flask import Flask, request, render_template, redirect, url_for, session, \
    flash
from models import db, User
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object('config')
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.drop_all()
    db.create_all()
    print('created tables')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show_users/')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        db.session.add(User(fname=form.fname.data,
                            sname=form.sname.data,
                            email=form.email.data,
                            password=generate_password_hash(form.password.data)))
        db.session.commit()
        redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        if _check_user_login(form):
            session['logged_in'] = True
            session['email'] = form.email.data
            return redirect(url_for('profile'))
        flash('Wrong email or password. Try again...', 'error')
        return redirect('login')
    return render_template('login.html', form=form)


@app.route('/profile/')
def profile():
    if 'logged_in' in session:
        return render_template('profile.html', email=session['email'])
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))


def _check_user_login(form: LoginForm):
    user = User.query.filter_by(email=form.email.data).first()
    return check_password_hash(user.password, form.password.data)


if __name__ == '__main__':
    app.run()
