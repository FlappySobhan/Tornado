from flask import request, jsonify, redirect, url_for
from core.exceptions import StructureError
from models.user import Users
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash


def login():
    """Login user"""
    if request.method == 'POST':
        try:
            phone = request.form.get('phone')
            print("================", str(phone), '================')
            password = request.form.get('login_password')
            print("================", str(password), '================')
            try:
                user = Users.get(Users.phone == phone)
                print("================", str(password), '================')
                print("================", str(user.password), '================')
                user_password_hash = generate_password_hash(password, method="pbkdf2:sha256")
                if user and check_password_hash(user.password, user_password_hash):
                    login_user(user)
                    return jsonify({'status': True, 'message': 'login successful'})
            except Exception as e:
                return jsonify({'status': False, 'message': 'login failed', 'err': str(e)})
        except Exception:
            return jsonify({'status': False, 'err': 'phone or password is wrong'}), 401
