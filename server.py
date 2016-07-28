#!/usr/bin/env python

"""Server run file.

Run by './server.py'
Access properties as 'config.property'
"""

import os, sys
from flask import Flask, send_file, render_template, request
from picamera import PiCamera
from time import sleep
import datetime, os

app = Flask(__name__)



tmp_dir = '/home/pi/images/'


def stamped_name(base_filename, fmt='%Y-%m-%d-%H-%M-%S_{base}'):
    return datetime.datetime.now().strftime(fmt).format(base=base_filename)

@app.route('/click')
def click():
    image_file = os.path.join(tmp_dir, stamped_name('image.jpg'))
    camera = PiCamera()
    camera.resolution = (2592, 1944)
    camera.capture(image_file)
    camera.close()
    return send_file(image_file, mimetype='image/jpeg')

@app.route('/')
def home():
    return 'hi'

app.run(debug=True, host='0.0.0.0', port=5001)
