from flask import render_template, redirect, url_for, session, request
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .user_model import User

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    # Retrieve the current user's gender
    current_user_gender = User.query.filter_by(id=session.get('id')).first().gender

    # Filter user profiles based on gender
    if current_user_gender == 'male':
        user_profiles = User.query.filter_by(gender='female').paginate(page=page, per_page=per_page, error_out=False)
    elif current_user_gender == 'female':
        user_profiles = User.query.filter_by(gender='male').paginate(page=page, per_page=per_page, error_out=False)
    else:
        # Handle case where gender is not specified or invalid
        user_profiles = []

    return render_template('home.html', user_profiles=user_profiles)
