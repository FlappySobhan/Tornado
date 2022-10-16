from flask import Flask
from decouple import config
from flask_login import LoginManager

from core.urls import routes
from core.router import Router
from core.utils import create_tables, GenerateData
from models.user import Users
from models.extra import Extra


if bool(config('IS_LOCAL', False)):
    # Create database tables
    create_tables()

    # Generate fake data
    GenerateData()

app = Flask(__name__)
app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
router = Router(app, routes)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        user = Users.get(Users.id == user_id)
        extra = Extra.select().where(Extra.user_id == user.id).first()
        if extra:
            user.extra = extra
        return user
    except Exception:
        return None


if __name__ == '__main__':
    app.run(host=config('HTTP_HOST', '127.0.0.1'), port=int(
        config('HTTP_PORT', '5005')), debug=bool(config('DEBUG', False)))
