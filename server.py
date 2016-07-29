#!/usr/bin/env python

"""Server run file.

Run by './server.py'
Access properties as 'config.property'
"""

import datetime
from flask import Flask, send_file
from picamera import PiCamera, PiCameraError
from io import BytesIO


app = Flask(__name__)


def stamped_name(base_filename, fmt='%Y-%m-%d-%H-%M-%S_{base}'):
    return datetime.datetime.now().strftime(fmt).format(base=base_filename)


@app.route('/click')
def click():
    new_file_name = stamped_name('image.jpg')
    image_stream = BytesIO()

    camera = PiCamera()

    camera.resolution = (2592, 1944)
    camera.capture(image_stream, 'jpeg')
    camera.close()

    return send_file(image_stream,
                     mimetype='image/jpeg',
                     attachment_filename=new_file_name)


@app.route('/')
def home():
    return 'hi'

app.run(debug=True, host='0.0.0.0', port=5001)
