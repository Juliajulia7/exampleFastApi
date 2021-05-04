import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Operation(Base):
    __tablename__ = 'tasks'

    id=sq.Column(sq.Integer, primary_key=True)
    date = sq.Column(sq.Date)
    uid=sq.Column(sq.Integer)
    title = sq.Column( sq.String(100))
    description = sq.Column( sq.Text)
    result = sq.Column(sq.String)

