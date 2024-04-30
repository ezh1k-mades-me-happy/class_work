from flask import Flask, render_template, redirect
from data import db_session
from data.jobs import Jobs
from data.users import User
from data.login_form import LoginForm
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'iAmTerminator'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/index')
@app.route('/')
def index():
    title = 'Главная'
    return render_template('index.html', title=title)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/order', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        return redirect('/success')
    return render_template('order.html', title='Авторизация', form=form)


def zapros():
    sess = db_session.create_session()
    for user in sess.query(User).filter(User.age == 21):
        print(user.name)
    sess.close()


def main1():
    db_name = 'db/blogs.db'
    db_session.global_init(db_name)
    sess = db_session.create_session()
    res = sess.query(User).all()
    for el in res:
        print(el)


def main():
    db_session.global_init("db/blogs.db")
    zapros()
    app.run('127.0.0.1', port=80)


if __name__ == '__main__':
    main()
