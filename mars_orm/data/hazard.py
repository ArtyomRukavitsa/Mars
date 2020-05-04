import sqlalchemy
from .db_session import SqlAlchemyBase

association_table = sqlalchemy.Table('jobs_to_hazard', SqlAlchemyBase.metadata,
    sqlalchemy.Column('jobs', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('jobs.id')),
    sqlalchemy.Column('hazard', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('hazard.id'))
)


class Hazard(SqlAlchemyBase):
    __tablename__ = 'hazard'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    category = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)