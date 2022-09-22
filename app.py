from flask import Flask
from decouple import config

from views.urls import routes
from views.utils import Router
from core.utils import create_tables

create_tables()

app = Flask(__name__)
app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
router = Router(app, routes)
