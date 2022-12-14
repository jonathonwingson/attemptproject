from flask import Blueprint, redirect, render_template, request, send_from_directory,flash
from App.models import  db
import json
from App.controllers import get_all_feed

from flask_login import logout_user, current_user

logout_views = Blueprint('logout_views', __name__, template_folder='../templates')

@logout_views.route('/logout')
def logout():
    logout_user()
    flash('User logged out')
    return render_template('login.html')
