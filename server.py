#!/usr/bin/env python

"""Server run file.

Run by './server.py'
Access properties as 'config.property'
"""

from flask import Flask, send_file
from picamera import PiCamera, PiCameraError
from io import BytesIO
import config
import utils


app = Flask(__name__)


@app.route('/click')
def click():

    # Create BytesIO stream for image capture
    image_stream = BytesIO()

    # Configure camera
    camera = PiCamera()
    camera.resolution = config.image_resolution

    camera.exif_tags['IFD0.Copyright'] = config.exif_copyright

    # Capture image to BytesIO stream
    camera.capture(image_stream, config.image_format)

    # Cleanup and shutdown camera
    camera.close()

    # Create dummy filename
    new_file_name = utils.stamped_name(config.name_base)

    # Return BytesIO stream as file using send_file
    return send_file(image_stream,
                     mimetype=config.image_mime,
                     attachment_filename=new_file_name)


@app.route('/')
def home():
    return 'hi'

app.run(debug=config.debug, host=config.server_host, port=config.server_port)
