import numpy as np
import cv2

def bytes_to_cv2(byte_arr_1):

    img = np.frombuffer(byte_arr_1, np.int8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    return img

def get_video_frame():
    #add exception
    camera = cv2.VideoCapture(0)

    while True:

       ret, frame = camera.read()
       encoded_frame = cv2.imencode('.jpg', frame)[1]
       yield (b'\r\n--frame\r\n'
             b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_frame) + b'\r\n\r\n')
       #yield (bytearray(encoded_frame))