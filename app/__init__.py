from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # SQLAlchemy Configuration
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'database_url'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

    return app
