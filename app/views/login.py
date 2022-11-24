from flask import request, jsonify, render_template
from models.user import Users
from flask_login import login_user
from werkzeug.security import check_password_hash


def login():
    """Login user if exists and password is correct"""
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        user = Users.select().where(Users.phone == phone).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return jsonify({'success': True})

        return jsonify({'success': False, 'err': 'اطلاعات وروردی صحیح نمی‌باشد'})
    return render_template('home.html')
