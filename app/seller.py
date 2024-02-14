from flask import Blueprint, render_template, request
from .user_model import User


seller_bp = Blueprint('seller', __name__)

@seller_bp.route('/seller')
def seller():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    # Retrieve all user profiles
    user_profiles = User.query.paginate(page=page, per_page=per_page)
    return render_template('seller.html', user_profiles=user_profiles)
