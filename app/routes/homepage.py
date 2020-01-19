from flask import Blueprint, request, Response, render_template, make_response
from wsgiref.headers import Headers
from models import compare_images
from utils.image_utils import get_video_frame

home_blueprint = Blueprint('home', __name__, template_folder="templates")

@home_blueprint.route('/', methods=['GET'])
def feed():

    return render_template('home.html')
