from flask_restful import Api, Resource
from flask import request
from user_repository import UserRepository

def create_api(app):
    api = Api(app)

    class UserResource(Resource):
        def get(self):
            users = UserRepository.get_all_users()
            return [{"id": user.id, "username": user.username, "name": user.name, "email": user.email, "rol": user.rol} for user in users]

        def post(self):
            data = request.get_json()  # Aquí el cambio
            new_user = UserRepository.create_user(data['username'], data['password'], data.get('name'), data.get('email'), data.get('image'), data.get('rol'))
            return {"id": new_user.id, "username": new_user.username, "name": new_user.name}

    class SingleUserResource(Resource):
        def get(self, user_id):
            user = UserRepository.get_user_by_id(user_id)
            if user is None:
                return {"message": "User not found"}, 404
            return {"id": user.id, "username": user.username, "name": user.name, "email": user.email, "rol": user.rol}

        def put(self, user_id):
            data = request.get_json()  # Aquí también el cambio
            user = UserRepository.update_user(user_id, data.get('username'), data.get('password'), data.get('name'), data.get('email'), data.get('image'))
            if user is None:
                return {"message": "User not found"}, 404
            return {"id": user.id, "username": user.username, "name": user.name, "email": user.email, "rol": user.rol}

        def delete(self, user_id):
            user = UserRepository.delete_user(user_id)
            if user is None:
                return {"message": "User not found"}, 404
            return {"message": "User deleted successfully"}

    class LoginResource(Resource):
        def post(self):
            data = request.get_json()  # Aquí también
            user = UserRepository.authenticate(data['username'], data['password'])
            if user:
                return {"id": user.id, "username": user.username, "rol": user.rol}
            return {"message": "Invalid username or password"}, 401

    api.add_resource(UserResource, '/users')
    api.add_resource(SingleUserResource, '/users/<int:user_id>')
    api.add_resource(LoginResource, '/login')

    return api
