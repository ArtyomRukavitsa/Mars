from flask import Blueprint, jsonify, request
from data import db_session
from data.users import User
import datetime

blueprint = Blueprint('users_api', __name__,
                            template_folder='templates')


@blueprint.route('/api/users', methods=['GET'])
def get_users():
    session = db_session.create_session()
    users = session.query(User).all()
    return jsonify(
        {
            'users': [item.to_dict() for item in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict()
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'surname', 'name', 'age', 'position', 'speciality',
                  'address', 'email', 'hashed_password', 'city_from']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    user = User(
        id=request.json['id'],
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        hashed_password=request.json['hashed_password'],
        city_from=request.json['city_from'],
        modified_date=datetime.datetime.now()
    )
    if session.query(User).filter(User.id == user.id).first():
        return jsonify({'error': 'Id already exists'})
    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    session.delete(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['PATCH'])
def change_user(user_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    try:
        if request.json['surname']: user.surname = request.json['surname']
    except KeyError:
        pass
    try:
        if request.json['name']: user.name = request.json['name']
    except KeyError:
        pass
    try:
        if request.json['age']: user.age = request.json['age']
    except KeyError:
        pass
    try:
        if request.json['position']: user.position = request.json['position']
    except KeyError:
        pass
    try:
        if request.json['speciality']: user.speciality = request.json['speciality']
    except KeyError:
        pass
    try:
        if request.json['address']: user.address = request.json['address']
    except KeyError:
        pass
    try:
        if request.json['hashed_password']:
            user.hashed_password = request.json['hashed_password']
            user.set_password(user.hashed_password)
    except KeyError:
        pass
    try:
        if request.json['city_from']: user.city_from = request.json['city_from']
    except KeyError:
        pass
    session.commit()
    return jsonify({'success': 'OK'})