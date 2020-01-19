from flask import Blueprint, request
from models import compare_images
from utils.image_utils import bytes_to_cv2

image_ops_blueprint = Blueprint('image_ops', __name__)

@image_ops_blueprint.route('/test', methods=['POST'])
def images_same():
    
    img_1 = bytes_to_cv2(request.files["img1"].stream.read())
    img_2 = bytes_to_cv2(request.files["img2"].stream.read())

    return {"same" : 1 if compare_images(img_1, img_2) else 0}

    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()