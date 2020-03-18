import os
from flask import Flask, render_template, redirect, jsonify, make_response
from flask_login import LoginManager, login_user, login_required, logout_user
from loginform import LoginForm, JobsForm, RegisterForm
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask_restful import Api
from data.jobs_resource import JobsResource, JobsListResource
from data.users_resource import UserResource, UsersListResource
import jobs_api
import users_api


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.register_blueprint(jobs_api.blueprint)  # Строчка для добавления REST-API из урока 1
    app.register_blueprint(users_api.blueprint)
    api.add_resource(JobsListResource, '/api/v2/jobs')
    api.add_resource(JobsResource, '/api/v2/jobs/<int:job_id>')
    api.add_resource(UsersListResource, '/api/v2/users')
    api.add_resource(UserResource, '/api/v2/users/<int:user_id>')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs)
    name, surname = [], []
    for job in jobs:
        for el in session.query(User).filter_by(id=job.team_leader):
            name.append(el.name)
            surname.append(el.surname)
    return render_template("index.html", jobs=jobs, name=name, surname=surname)


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
        if form.validate_on_submit():
            session = db_session.create_session()
            job = Jobs()
            job.team_leader = form.team_leader.data
            job.job = form.job.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.is_finished = form.is_finished.data
            session.add(job)
            session.commit()
            return redirect("/")
        return redirect('/logout')
    return render_template('addjob.html', title='Добавление работы', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            hashed_password=form.password.data,
            age=form.age.data,
            speciality=form.speciality.data,
            address=form.address.data,
            position=form.position.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()
