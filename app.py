from flask import Flask
from decouple import config

from views.urls import routes
from views.utils import Router
from model.configs import db
from model.user import Users
from model.menu import Menu
from model.ingredient import Ingredient
from model.desk import Desk
from model.recipe import Recipe
from model.receipts import Receipts
from model.order import Order
from model.extra import Extra
from model.accounting import Accounting


db.create_tables([Users, Menu, Ingredient, Desk, Recipe,
                 Receipts, Order, Extra, Accounting])

app = Flask(__name__)
app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
router = Router(app, routes)
