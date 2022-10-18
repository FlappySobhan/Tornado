from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from models.user import Users
from models.rule import Rule


@login_required
def dashboard_employee():
    """Show employee panel"""
    if current_user.rule == "کارمند":
        return render_template('admin-panel.html', result=[])
    return render_template('admin-panel.html', result=[])


@login_required
def dashboard_admin():
    if current_user.rule.rule == "ادمین":
        user = [i for i in Users.select()]
        rule = [i for i in Rule.select()]
        return render_template('admin-panel.html', result=[user, rule])

    elif current_user.rule.rule == "کارمند":
        return redirect(url_for('employee_panel'))

    else:
        return redirect(url_for('dashboard'))
