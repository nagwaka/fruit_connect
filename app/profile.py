from flask import render_template, redirect, url_for, session, request
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from . import db
from .user_model import User
from .forms import EditProfileForm
from flask_babel import _


profile_bp = Blueprint('profile', __name__)
edit_profile_bp = Blueprint('edit_profile', __name__)

@profile_bp.route('/profile')
def profile():
    # Check if the user is logged in
    if 'loggedin' in session:
        # Acount info for the user to display on the profile page
        user = User.query.filter_by(id=session['id']).first()

        # Show the profile page with account info
        return render_template('profile.html', account=user)
    # User is not logged in redirect to login page
    return redirect(url_for('login.login'))



@edit_profile_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('edit_profile.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=_('Edit Profile'),
                           form=form)
