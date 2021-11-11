from flask import Flask, request, Response
import numpy as np
from cv2 import cv2
import requests


def get_watermark_image(img):
    try:
        addr = 'http://localhost:5000'
        test_url = addr + '/api/test'
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}

        r = requests.post(test_url, data=img.tostring(), headers=headers)
        r.raise_for_status()
        nparr = np.fromstring(r.content, np.uint8)
        im = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return im

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    raise SystemExit(err)

app = Flask(__name__)
app.debug = True


@app.route('/api/test', methods=['POST'])
def test():
    r = request
    print(1)
    nparr = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # resize here
    img_resized = img
    print(2)
    result_image = get_watermark_image(img_resized)
    print(3)
    return Response(result_image.tostring())


app.run(host="0.0.0.0", port=3000)
