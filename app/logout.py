from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from . import db
from .user_model import User
import re
import hashlib
from flask_bcrypt import Bcrypt
from flask import session

bcrypt = Bcrypt()


logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    # Log the user out using Flask-Login
    logout_user()

    # Redirect to login page
    return redirect(url_for('index.index'))
