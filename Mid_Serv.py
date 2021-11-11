from flask import Flask, request, Response
import numpy as np
from cv2 import cv2
import os
import requests

app = Flask(__name__)
app.debug = True


@app.route('/api/test2', methods=['POST'])
def test():
    r = request

    nparr = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # resize here
    img_resized = img

    return Response(img_resized.tostring())


app.run(host="0.0.0.0", port=5000)
