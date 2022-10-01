from flask import render_template, request, jsonify, redirect, url_for
from core.exceptions import StructureError
from models.user import Users
from models.rule import Rule

x = Rule("admin")
x.save()


def login_us():
    return render_template("form.html")


def login():
    if request.method == 'POST':
        # Get the form data

        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        phone = request.form.get('phone')
        address = request.form.get('address')
        password = request.form.get('password')
        # Send the message
        try:
            user = Users(firstname, lastname, phone, address, password, 0, 0)
            user.save()
        except StructureError as e:
            return jsonify({'success': False, 'err': str(e)})
        except Exception:
            return jsonify({'success': False, 'err': 'این کاربر پیش‌تر ثبت‌نام کرده است'})
        else:
            return jsonify({'success': True})
    return redirect(url_for('login_us'))
