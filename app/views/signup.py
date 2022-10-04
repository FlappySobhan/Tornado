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
        # Send the message
        try:
            user = Users(firstname, lastname, phone, address, password, 0, 0, 1)
            x = Users.select().where(Users.phone == phone)[Users.phone]
            print(x)
            if x:
                return jsonify({'success': False, 'err': 'این کاربر پیش‌تر ثبت‌نام کرده است'})
        except StructureError as e:
            return jsonify({'success': False, 'err': str(e)})
        else:
            user.save()
            return jsonify({'success': True})
    return redirect(url_for('home'))
