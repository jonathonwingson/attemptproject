from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.models import User

from App.controllers import (
    create_feed,
    get_all_feed,
    create_dist
)

feed_views = Blueprint('feed_views', __name__, template_folder='../templates')


@feed_views.route('/api/feed', methods=['GET'])
def create_feed_action():
    
    users=User.query.all()
    numprofiles=len(users)
    dist = create_dist(numprofiles)
    
    for user in users:
        feed = create_feed( user.id , dist.id )

    
    return jsonify({"message":"distributed"})



#for UI
@feed_views.route('/api/feeds', methods=['GET'])
def view_all_feed():
    feeds = get_all_feed()
    return render_template('feed.html', feeds=feeds)