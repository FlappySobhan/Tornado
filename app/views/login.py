from flask import request, jsonify, redirect, url_for
from core.exceptions import StructureError
from models.user import Users
from flask_login import login_user, logout_user, login_required, current_user


@login_manager.request_loader
def login():
    """Login user"""
    try:
        phone = request.form.get('phone')
        password = request.form.get('password')
        user = Users.get(Users.phone == phone)
        if user and user.check_password(password):
            login_user(user)
            return jsonify({'status': True, 'message': 'login successful'})
        else:
            return jsonify({'status': False, 'message': 'phone or password is wrong'}), 401
    except Users.DoesNotExist:
        return jsonify({'message': 'نام کاربری یا رمز عبور اشتباه است'}), 401
    except StructureError as e:
        return jsonify({'message': e.message}), 400
