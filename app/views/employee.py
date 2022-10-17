from flask import render_template, request
from models.user import Users
from models.rule import Rule


def dashboard_employee():
    if request.method == 'GET':
        user = []
        rule = []
        query = Users.select()
        for i in query:
            user.append(i)
        query = Rule.select()
        for i in query:
            rule.append(i)
        return render_template('admin-panel.html', result=[user, rule])
