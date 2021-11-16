from flask import Flask, request, Response
import numpy as np
from cv2 import cv2
from make_watermark_on_photo import watermark_photo
from save_instruments import save_original_image, add_to_origin_table
import os

# Creating flask server
app = Flask(__name__)
app.debug = False


@app.route('/api/test', methods=['POST'])
def test():
    r = request

    nparr = np.fromstring(r.data, np.uint8)
    filename = 'base_img.jpg'
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    counter = save_original_image(img, filename)
    extension = filename.find('.')
    add_to_origin_table(filename)
    path_to_original = os.path.abspath(os.curdir) + '\\Original\\' + filename[:extension] + str(counter) + filename[
                                                                                                           extension:]
    edited_name = 'edited.jpg'

    path_to_watermark = "w.png"

    return Response(img_encoded.tostring())


# run flask server
app.run(host="0.0.0.0", port=5000)
