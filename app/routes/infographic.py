from flask import Blueprint, request, Response, render_template, make_response
from models import compare_images

graphic_blueprint = Blueprint('graphic', __name__, template_folder="templates")

@graphic_blueprint.route('/graphic', methods=['POST'])
def feed():

    start_pos = request.form.start_pos
    destination_pos = request.form.destination_pos

    print(request.form)
    return render_template('graphic.html')