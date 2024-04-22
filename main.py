from flask import Flask, render_template, redirect
from data import db_session
from data.jobs import Jobs
from data.users import User
from data.login_form import LoginForm
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/index')
@app.route('/')
def index():
    title = 'Главная'
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<type>')
def profession(type):
    profs = ['слесарь'] * 15
    profs = [j + ' ' + str(i + 1) for i, j in enumerate(profs)]
    return render_template('prof.html', list=profs, type=type)


@app.route('/form1', methods=['GET', 'POST'])
def registr():
    return render_template('form1.html')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


def login_user(user, remember_me=False):
    pass


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


def add_user():
    sess = db_session.create_session()
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    user.hashed_password = '123'
    sess.add(user)
    sess.commit()
    sess.close()


def add_jobs():
    sess = db_session.create_session()
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    sess.add(job)
    sess.commit()
    sess.close()


def main():
    db_session.global_init("db/blogs.db")
    zapros()
    app.run('127.0.0.1', port=80)
    # add_user()
    # add_jobs()


if __name__ == '__main__':
    main()