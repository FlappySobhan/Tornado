from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user, logout_user
from decouple import config
from re import match
from werkzeug.security import check_password_hash

from models.user import Users
from models.extra import Extra
from models.order import Order
from models.status import Status
from core.exceptions import StructureError


@login_required
def dashboard():
    return render_template('dashboard.html')


@login_required
def edit_user():
    """Edit user info"""
    if request.method == 'POST':
        update_user = {'name': request.form['name'], 'family': request.form['family'],
                       'address': request.form['address']}
        update_extra = {'email': request.form['email'], 'phone': request.form['phone2'],
                        'address': request.form['address2'],
                        'info': request.form['info'], 'user': current_user.id}

        try:
            Users(**update_user, phone=current_user.phone, password=config('SECURITY_PASS_TEST'),
                  balance=current_user.balance,
                  subscription=current_user.subscription, rule=current_user.rule)
            Extra(**update_extra)
        except StructureError as e:
            return jsonify({'success': False, 'err': f"{e}"})
        else:
            for key, value in update_user.items():
                Users.update({key: value}).where(Users.id == current_user.id).execute()
            extra_check = Extra.select().where(Extra.user == current_user.id).first()
            if extra_check:
                for key, value in update_extra.items():
                    Extra.update({key: value}).where(Extra.user_id == current_user.id).execute()
            else:
                Extra.create(**update_extra)
            return jsonify({'success': True, 'err': "اطلاعات با موفقیت ثبت شد"})

    return redirect(url_for('dashboard'))


@login_required
def order_history():
    """Show order history"""
    if request.method == 'GET':
        orders = []
        query = Order.select().where(Order.user == current_user.id)
        counter = 1
        for i in query:
            order = i.__dict__['__data__']
            order.update(count=counter)
            orders.append(order)
            counter += 1
        orders = map(lambda x: {**x, 'status': Status.select().where(Status.id == x['status']).first().status}, orders)

        return render_template('order_history.html', result=orders)


@login_required
def logout():
    """Logout"""
    logout_user()
    return redirect(url_for('home'))


@login_required
def change_password():
    """Change password"""
    if request.method == 'POST':
        old_pass = request.form['old_pass']
        new_pass = request.form['new_pass']
        password_pattern = Users.patterns['password']
        if check_password_hash(current_user.password, old_pass):
            if match(password_pattern, new_pass):
                Users.update({Users.password: new_pass}).where(Users.id == current_user.id).execute()
                return jsonify({'success': True, 'err': 'رمز عبور با موفقیت تغییر کرد'})
            else:
                return jsonify({'success': False, 'err': 'رمز عبور باید حداقل ۸ کاراکتر باشد'})
        else:
            return jsonify({'success': False, 'err': 'رمز عبور فعلی صحیح نمی‌باشد'})

    return render_template('change_password.html')


