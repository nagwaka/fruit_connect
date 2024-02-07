from flask import render_template, redirect, url_for, session
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .user_model import User

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    # Check if the user is logged in
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login.login'))
