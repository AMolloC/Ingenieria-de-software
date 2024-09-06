from user import db, User
from werkzeug.security import generate_password_hash

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create_user(username, password, name=None, email=None, image=None, rol='user'):
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, name=name, email=email, image=image, rol=rol)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update_user(user_id, username=None, password=None, name=None, email=None, image=None):
        user = User.query.get(user_id)
        if user:
            if username:
                user.username = username
            if password:
                user.password = generate_password_hash(password)
            if name:
                user.name = name
            if email:
                user.email = email
            if image:
                user.image = image
            db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.passwordValid(password):
            return user
        return None
