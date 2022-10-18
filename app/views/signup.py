from flask import request, jsonify, redirect, url_for
from core.exceptions import StructureError
from models.user import Users


def signup():
    if request.method == 'POST':

        # Get the form data
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        phone = request.form.get('phone')
        address = request.form.get('address')
        password = request.form.get('password')

        # search for the user and return error if he is duplicated
        if Users.select().where(Users.phone == phone):
            return jsonify({'success': False, 'err': 'این کاربر پیش‌تر ثبت‌نام کرده است'})

        # create new user if data is valid
        try:
            subs = Users.select().order_by(Users.id.desc()).first()
            subs = subs.id + 1 if subs else 100
            user = Users(firstname, lastname, phone, address, password, 0, subs, 1)
        except StructureError as e:
            return jsonify({'success': False, 'err': str(e)})
        else:
            user.save()
            return jsonify({'success': True})

    return redirect(url_for('home'))
