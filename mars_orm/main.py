from flask import Flask, render_template, redirect, request, make_response, session
from flask_login import LoginManager, login_user, login_required, logout_user
from loginform import LoginForm, JobsForm
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    # user = User()
    # user.surname = "Scott"
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # user.email = "scott_chief@mars.org"
    # user.hashed_password = "cap"
    # user.set_password(user.hashed_password)
    # session = db_session.create_session()
    # session.add(user)
    # session.commit()

    # user = User()
    # user.surname = "Sun"
    # user.name = "Rules"
    # user.age = 34
    # user.position = "marsohod"
    # user.speciality = "engineer"
    # user.address = "module_2"
    # user.email = "sun_chief@mars.org"
    # user.hashed_password = "mars"
    # session = db_session.create_session()
    # session.add(user)
    # session.commit()
    #
    # jobs = Jobs()
    # jobs.team_leader = 1
    # jobs.job = 'deployment of residential modules 1 and 2'
    # jobs.work_size = 15
    # jobs.collaborators = '2, 3'
    # session = db_session.create_session()
    # session.add(jobs)
    # session.commit()

    app.run()


@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session()
    jobs = []
    for user in session.query(Jobs).all():
        jobs.append(user)
        print(jobs)
    session.commit()
    return render_template('index.html', jobs=jobs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/addjob', methods=['GET', 'POST'])
def addjob():
    form = JobsForm()
    if form.validate_on_submit():
        if session:
            return redirect("/")
        return redirect('/logout')
    return render_template('addjob.html', title='Добавление работы', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()
