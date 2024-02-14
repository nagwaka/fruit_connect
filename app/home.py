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

    # Retrieve all user profiles except the current user's profile
    user_profiles = User.query.filter(User.id != session.get('id')).paginate(page=page, per_page=per_page, error_out=False)
    return render_template('home.html', user_profiles=user_profiles)
