from flask import Flask, request, Response
import numpy as np
from cv2 import cv2
from resize_image import resize_img
import requests


def get_watermark_image(img):
    try:
        addr = 'http://localhost:5000'
        test_url = addr + '/api/test'
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}
        _, img_encoded = cv2.imencode('.jpg', img)
        r = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
        r.raise_for_status()
        nparr = np.fromstring(r.content, np.uint8)
        im = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return im
    except requests.exceptions.HTTPError as e:
        return e.response.status_code
    except requests.exceptions.ConnectionError:
        return "ConnectionError"
    except requests.exceptions.Timeout:
        return "TimeoutError"
    except requests.exceptions.RequestException:
        return "OtherError"


app = Flask(__name__)
app.debug = False


@app.route('/api/test', methods=['POST'])
def test():
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_resized = resize_img(img)
    result_image = get_watermark_image(img_resized)
    if isinstance(result_image, (int, str)):
        return Response(status=result_image)
    return Response(result_image.tostring())


app.run(host="0.0.0.0", port=3000)
