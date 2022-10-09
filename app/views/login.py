from flask import request, jsonify, redirect, url_for
from core.exceptions import StructureError
from models.user import Users
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash


def login():
    """Login user"""
    if request.method == 'POST':
        try:
            phone = request.form['phone']
            password = request.form['password']
        except KeyError:
            return jsonify({'error': 'Invalid data'})

        try:
            user = Users.get(Users.phone == phone)
        except Users.DoesNotExist:
            return jsonify({'success': False, 'err': 'کاربر یافت نشد'})
        try:
            if check_password_hash(user.password, password):
                login_user(user)
                return jsonify({'success': True})
        except Exception:
                return jsonify({'success': False, 'err': 'رمز عبور اشتباه است'})
        else:
            return jsonify({'success': False, 'err': 'رمز عبور اشتباه است'})

