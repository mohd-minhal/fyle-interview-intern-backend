from flask import Blueprint, jsonify, request
from core.models.users import User

user_api = Blueprint('user_api', __name__)

@user_api.route('/principal/users/filter', methods=['GET'])
def filter_users():
    username = request.args.get('username')
    email = request.args.get('email')

    filters = []
    if username:
        filters.append(User.username == username)
    if email:
        filters.append(User.email == email)

    # Retrieve users based on filters
    users = User.filter(*filters).all() if filters else User.filter().all()
    return jsonify({'data': [user.to_dict() for user in users]}), 200

@user_api.route('/principal/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.get_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'data': user.to_dict()}), 200

@user_api.route('/principal/users/email/<string:email>', methods=['GET'])
def get_user_by_email(email):
    user = User.get_by_email(email)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'data': user.to_dict()}), 200
