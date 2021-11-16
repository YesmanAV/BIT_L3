from flask import Flask, request, Response
import numpy as np
from cv2 import cv2
from make_watermark_on_photo import watermark_photo
from save_instruments import save_original_image, add_to_origin_table
import os

app = Flask(__name__)
app.debug = False
app.run(host="0.0.0.0", port=5000)
