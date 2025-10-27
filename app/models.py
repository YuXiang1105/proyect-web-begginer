from . import db
from sqlalchemy import *

class Alien(db.Model):
    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Danger =  db.Column(db.String(100), nullable=False)
    Class = db.Column(db.String(100), nullable=False)
    Origin = db.Column(db.String(100), nullable=True)
    Description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Relic: {self.Name} - {self.Description}'