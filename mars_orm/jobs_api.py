from flask import Blueprint, jsonify, request
from data import db_session
from data.jobs import Jobs

blueprint = Blueprint('jobs_api', __name__,
                            template_folder='templates')


@blueprint.route('/api/jobs', methods=['GET'])
def get_job():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'team_leader', 'job', 'collaborators',
                                    'start_date', 'end_date', 'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=('id', 'team_leader', 'job', 'collaborators',
                                       'start_date', 'end_date', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    job = Jobs(
        id=request.json['id'],
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        # start_date=request.json['start_date'],
        # end_date=request.json['end_date'],
        is_finished=request.json['is_finished']
    )
    if session.query(Jobs).filter(Jobs.id == job.id).first():
        return jsonify({'error': 'Id already exists'})
    session.add(job)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    session.delete(jobs)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PATCH'])
def change_jobs(jobs_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    session = db_session.create_session()
    job = session.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    try:
        if request.json['job']: job.job = request.json['job']
    except KeyError:
        pass
    try:
        if request.json['collaborators']: job.collaborators = request.json['collaborators']
    except KeyError:
        pass
    try:
        if request.json['team_leader']: job.team_leader = request.json['team_leader']
    except KeyError:
        pass
    try:
        if request.json['work_size']: job.work_size = request.json['work_size']
    except KeyError:
        pass
    try:
        if request.json['is_finished']: job.job = request.json['is_finished']
    except KeyError:
        pass
    session.commit()
    return jsonify({'success': 'OK'})