from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user, logout_user
from decouple import config
from werkzeug.security import check_password_hash

from models.user import Users
from models.extra import Extra
from models.order import Order
from core.exceptions import StructureError


@login_required
def dashboard():
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
            Users.update(update_user).where(Users.id == current_user.id).execute()
            extra_check = Extra.select().where(Extra.user == current_user.id).first()
            if extra_check:
                Extra.update(update_extra).where(Extra.user_id == current_user.id).execute()
            else:
                Extra.create(**update_extra)
            return jsonify({'success': True, 'err': "اطلاعات با موفقیت ثبت شد"})

    return render_template('dashboard.html')


@login_required
def order_history():
    """Show order history"""
    if request.method == 'GET':
        query = Order.select().where(Order.user == current_user.id)
        orders = [order for order in query]

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
        old_pass = request.form['oldPassword']
        new_pass = request.form['newPassword']
        if check_password_hash(current_user.password, old_pass):
            try:
                user = Users('jeff', 'bobs', '09123536842',
                             'iran-mashhad', new_pass, 12345, 12345, 2)
            except StructureError:
                return jsonify({'success': False,
                                'err': 'رمز عبور باید حداقل ۸ کاراکتر و شامل حروف خاص، بزرگ و کوچک و اعداد باشد.'})
            else:
                Users.update({Users.password: user.password}).where(Users.id == current_user.id).execute()
                return jsonify({'success': True, 'err': 'رمز عبور با موفقیت تغییر یافت'})
        else:
            return jsonify({'success': False, 'err': 'رمز عبور قبلی صحیح نمی‌باشد'})

    return render_template('change_password.html')
