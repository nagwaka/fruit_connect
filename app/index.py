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


index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')
