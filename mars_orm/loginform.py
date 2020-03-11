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
    is_finished = BooleanField('Статус', default=False)
    submit = SubmitField('Войти')