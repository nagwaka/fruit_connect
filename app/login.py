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


login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Output a message if something goes wrong...
    msg = ''

    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        # Retrieve the user from the database
        user = User.query.filter_by(username=username).first()

        # Check if the user exists and the password is correct
        if user and bcrypt.check_password_hash(user.password, password):
            # Log the user in and create session data
            login_user(user)
            session['loggedin'] = True
            session['id'] = user.id
            session['username'] = user.username

            # Redirect to home page
            return redirect(url_for('home.home'))
        else:
            # Account doesn't exist or username/password incorrect
            msg = 'Incorrect username or password!'

    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)
