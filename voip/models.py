import datetime as dt

from . app import db

class Commands(db.Model):
    __tablename__ = 'commands'

    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(60), index=True)

    delivered = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)

    def __repr__(self):
        return '<Command: {}>'.format(self.command)
