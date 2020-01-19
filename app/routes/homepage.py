from flask import Blueprint, request, Response, render_template, make_response, url_for
from wsgiref.headers import Headers

home_blueprint = Blueprint('home', __name__, template_folder="templates")

@home_blueprint.route('/', methods=['GET'])
def feed():
    return render_template('home.html')
