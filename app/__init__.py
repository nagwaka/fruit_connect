from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_migrate import Migrate
import os


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load environment variables
    SECRET_KEY = os.environ['SECRET_KEY']
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '3306')
    DB_NAME = os.environ['DB_NAME']
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    # SQLAlchemy Configuration
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    # Set Flask app config
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Define the user_loader callback
    @login_manager.user_loader
    def load_user(user_id):
        from .user_model import User
        return User.query.get(int(user_id))

    from .login import login_bp
    app.register_blueprint(login_bp)

    from .logout import logout_bp
    app.register_blueprint(logout_bp)

    from .home import home_bp
    app.register_blueprint(home_bp)

    from .profile import profile_bp
    app.register_blueprint(profile_bp)

    from .signup import signup_bp
    app.register_blueprint(signup_bp)

    from .index import index_bp
    app.register_blueprint(index_bp)

    from .seller import seller_bp
    app.register_blueprint(seller_bp)

    return app
