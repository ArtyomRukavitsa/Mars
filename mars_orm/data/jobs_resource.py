from flask import jsonify
from flask_restful import abort, Resource, reqparse
from data.jobs_parser import parser
from data import db_session
from data.jobs import Jobs
import datetime


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict()})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

    def patch(self, job_id):
        abort_if_job_not_found(job_id)
        # Для изменения данных нужен другой парсер, так как нам необязательно, чтобы "прилетал" каждый параметр
        parser = reqparse.RequestParser()
        parser.add_argument('team_leader')
        parser.add_argument('job')
        parser.add_argument('work_size', type=int)
        parser.add_argument('collaborators')
        parser.add_argument('is_finished', type=bool)
        args = parser.parse_args()
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        try:
            if args['team_leader']: job.team_leader = args['team_leader']
        except Exception:
            pass
        try:
            if args['job']: job.job = args['job']
        except Exception:
            pass
        try:
            if args['work_size']: job.work_size = args['work_size']
        except Exception:
            pass
        try:
            if args['is_finished']: job.is_finished = args['is_finished']
        except Exception:
            pass
        try:
            if args['collaborators']: job.collaborators = args['collaborators']
        except Exception:
            pass
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [job.to_dict() for job in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=datetime.datetime.now(),
            end_date=datetime.datetime.now(),
            is_finished=args['is_finished']
            )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})

