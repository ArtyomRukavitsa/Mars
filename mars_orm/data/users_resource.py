from flask import jsonify
from flask_restful import abort, Resource
from data.users_parser import parser
from data import db_session
from data.users import User
import datetime


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('surname', 'name', 'position', 'speciality', 'email'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [user.to_dict(
            only=('surname', 'name', 'position', 'speciality', 'email')) for user in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(surname=args['surname'],
                    name=args['name'],
                    age=args['age'],
                    position=args['position'],
                    speciality=args['speciality'],
                    address=args['address'],
                    email=args['email'],
                    hashed_password=args['hashed_password'],
                    modified_date=datetime.datetime.now()
                    )
        user.set_password(user.hashed_password)
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})