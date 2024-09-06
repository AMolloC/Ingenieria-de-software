from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    image = db.Column(db.String(200))
    rol = db.Column(db.String(50), default='user')

    def updateProfile(self, name=None, email=None, image=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if image:
            self.image = image
        db.session.commit()

    def passwordValid(self, password):
        return check_password_hash(self.password, password)
