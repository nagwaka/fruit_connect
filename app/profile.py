from flask import render_template, redirect, url_for, session
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .user_model import User


profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile/<int:user_id>')
def profile(user_id):
    # Retrieve the user profile using the provided user_id
    user = User.query.get(user_id)
    if user:
        return render_template('profile.html', account=user)
    else:
        # Handle case where user is not found
        flash("User not found.", "error")
        return redirect(url_for('home.home'))
