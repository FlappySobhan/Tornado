from flask import render_template, request
from models.menu import Menu


def menu():
    if request.method == 'GET':
        menu = []
        query = Menu.select()
        for i in query:
            menu.append(i)
        return render_template('menu.html', result=menu)
