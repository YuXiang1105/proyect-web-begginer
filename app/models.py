from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import *
from flask_login import UserMixin

class AlienClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    aliens = db.relationship(
        "Alien",
        secondary="alien_class_relation",
        back_populates="classes"
    )
    def __repr__(self):
        return f"AlienClass: {self.name}"

alien_class_relation = db.Table(
    'alien_class_relation',
    db.Column('alien_id', db.Integer, db.ForeignKey('alien.Id'), primary_key=True),
    db.Column('class_id', db.Integer, db.ForeignKey('alien_class.id'), primary_key=True)
)


class Alien(db.Model):
    Id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Name = db.Column(db.String(100), nullable=False)
    Danger =  db.Column(db.String(100), nullable=False)
    Origin = db.Column(db.String(100), nullable=True)
    Description = db.Column(db.Text, nullable=False)
    classes = db.relationship(
    "AlienClass",
    secondary=alien_class_relation,
    back_populates="aliens"
)


    def __repr__(self):
        return f'Relic: {self.Name} - {self.Description}'
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    aliens = db.relationship("Alien", backref="creator", lazy=True)
    password_hash = db.Column(db.String)
    
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'User: {self.email}'
    
@login_manager.user_loader
def load_user(user_id):
 return User.query.get(int(user_id))