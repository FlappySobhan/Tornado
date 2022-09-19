from flask import Flask
from decouple import config

from views.urls import routes
from views.utils import Router

# from model.order import Order
from model.accounting import Accounting
Accounting(100, 'hello', 1)

app = Flask(__name__)
app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
router = Router(app, routes)
