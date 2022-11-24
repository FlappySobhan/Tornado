from flask import render_template
from models.menu import Menu


def menu():
    query = Menu.select()
    menu_list = [m for m in query]
    return render_template('menu.html', result=menu_list)
