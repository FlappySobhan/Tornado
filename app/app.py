from flask import Flask
from decouple import config
from flask_login import LoginManager

from core.urls import routes
from core.router import Router
from core.utils import create_tables, generate_data

if bool(config('IS_LOCAL', False)):
    # Create database tables
    create_tables()

    # Generate fake data
    generate_data()

app = Flask(__name__)
app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
router = Router(app, routes)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'لظفا ابتدا وارد شوید'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)




if __name__ == '__main__':
    app.run(host=config('HTTP_HOST', '127.0.0.1'), port=int(
        config('HTTP_PORT', '5005')), debug=bool(config('DEBUG', False)))
