from flask import render_template, redirect, url_for, session
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .user_model import User


profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
def profile():
    # Check if the user is logged in
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        user = User.query.filter_by(id=session['id']).first()

        # Show the profile page with account info
        return render_template('profile.html', account=user)
    # User is not logged in redirect to login page
    return redirect(url_for('login.login'))
