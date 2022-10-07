from flask import render_template, request


def home():
    if request.method == 'GET':
        return render_template('home.html')
