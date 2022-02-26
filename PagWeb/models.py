from email.policy import default
from . import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

'''
class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), default=None)
    key = db.Column(db.String(25), default=None)
    rsh_estado= db.relationship('Municipio', lazy=True, cascade="all, delete", backref=db.backref('estado', lazy=True))

class Municipio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), default=None)
    key = db.Column(db.String(25), default=None)
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id'))
    municipio= db.relationship('Colonia', lazy=True, cascade="all, delete", backref=db.backref('municipio', lazy=True))

class Colonia(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cp = db.Column(db.Integer, default = 0)
    name = db.Column(db.String(25), default = None)
    key = db.Column(db.String(25), default = None)
    colonia_id = db.Column(db.Integer, db.ForeignKey('municipio.id'))
'''