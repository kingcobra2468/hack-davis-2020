from flask import Blueprint, request, Response, render_template, make_response
from wsgiref.headers import Headers
from models import compare_images
from utils.image_utils import get_video_frame

image_feed_blueprint = Blueprint('image_feed', __name__, template_folder="templates")

@image_feed_blueprint.route('/feed-raw', methods=['GET'])
def mjpeg_stream():
    
    headers = {'Content-Type': 'multipart/x-mixed-replace; boundary=frame'}
    
    return Response(get_video_frame(), headers = headers) #mimetype='multipart/x-mixed-replace;boundary=frame')

@image_feed_blueprint.route('/feed', methods=['GET'])
def feed():

    return render_template('camera_feed.html')