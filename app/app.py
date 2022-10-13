from flask import Flask
from decouple import config
from flask_login import LoginManager

from core.urls import routes
from core.router import Router
from core.utils import create_tables, generate_data
from models.user import Users

if bool(config('IS_LOCAL', False)):
    # Create database tables
    create_tables()

    # Generate fake data
    generate_data()

app = Flask(__name__)
app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
router = Router(app, routes)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        return Users.get(Users.id == user_id)
    except Exception:
        return None


if __name__ == '__main__':
    app.run(host=config('HTTP_HOST', '127.0.0.1'), port=int(
        config('HTTP_PORT', '5005')), debug=bool(config('DEBUG', False)))
