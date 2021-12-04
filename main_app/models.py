from datetime import datetime

from main_app import db


from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from main_app import login

class User(UserMixin, db.Model):


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique= True, index=True)    
    email = db.Column(db.String(128), unique= True, index=True)
    password_hash = db.Column(db.String(128))  
    posts = db.relationship('Posts', backref='author', lazy='dynamic')  

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Posts(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index= True , default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'Post {self.body}'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

