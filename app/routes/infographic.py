from flask import Blueprint, request, Response, render_template, make_response
from utils.transport_data import TransportData
from config import GOOGLE_API_KEY

graphic_blueprint = Blueprint('graphic', __name__, template_folder = "templates")

@graphic_blueprint.route('/graph', methods = ['POST'])
def feed():

    start_pos = request.form["start_pos"]
    destination_pos = request.form["destination_pos"]
    transport_data = TransportData(GOOGLE_API_KEY, start_pos, destination_pos)

    return render_template('graph.jinja', api_key = GOOGLE_API_KEY, start_pos = start_pos, destination_pos = destination_pos, 
        transport_distance = transport_data.get_transport_distances(), transport_times = transport_data.get_times(),
        transport_co2 = transport_data.get_co2(), transport_kwh = transport_data.get_kwh())