from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired
import datetime


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class JobsForm(FlaskForm):
    team_leader = IntegerField('id руководителя', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField('Длительность работы', validators=[DataRequired()])
    collaborators = StringField('Список id участников', validators=[DataRequired()])
    start_date = DateField('Время начала работы', default=datetime.datetime.now)
    end_date = DateField('Время конца работы', default=datetime.datetime.now)
    hazard = IntegerField('Категория работы', validators=[DataRequired()])
    is_finished = BooleanField('Работа завершена', default=False)
    submit = SubmitField('Добавить')


class RegisterForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    age = IntegerField('Ваш возраст', validators=[DataRequired()])
    position = StringField("Ваша должность", validators=[DataRequired()])
    speciality = StringField("Ваша специальность", validators=[DataRequired()])
    address = StringField("Ваш адрес", validators=[DataRequired()])
    submit = SubmitField('Зарегитрироваться')


class DepartmentForm(FlaskForm):
    title = StringField('Название департамента', validators=[DataRequired()])
    chief = IntegerField('id шеф', validators=[DataRequired()])
    members = StringField('Список id участников', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired()])
    submit = SubmitField('Добавить')