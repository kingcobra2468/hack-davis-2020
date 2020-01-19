from flask import Blueprint, request, Response, render_template, make_response
from os import popen
from hashlib import md5
import json
discovery_blueprint = Blueprint('discovery', __name__)

def get_ip_addr():
   
    ip_addr = popen("ifconfig wlp3s0 | tr -s ' ' | egrep -m 1 \"inet ([0-9]{1,3}[.]?)*\" | cut -f 3 -d ' '").read()
    
    if ip_addr is not '':
        ip_addr = ip_addr.rstrip()

    return ip_addr

@discovery_blueprint.route('/discovery', methods=['GET'])
def mjpeg_stream():
       
    data = {'status' : 'ok', 'cam_id' : ''}

    ip_addr = get_ip_addr()
    
    if ip_addr is '':

        data['status'] = 'failed'
        return make_response(json.dumps(data), 500, {'Content-Type': 'application/json'})

    else:
        
        ip_addr = ip_addr.rstrip()
        data['cam_id'] = md5(bytes(ip_addr.encode())).hexdigest()
        return make_response(json.dumps(data), 200, {'Content-Type': 'application/json'})