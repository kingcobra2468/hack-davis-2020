import cv2

def compare_images(img1, img2):

    #not smart comparison for now, images must be same size
    #maybe once I get enough opencv scaling knowledge, check if schaling could be the same
    if img1.shape != img2.shape:
        return False

    output = cv2.bitwise_xor(img1,img2)
    return not output.any()