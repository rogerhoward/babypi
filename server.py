#!/usr/bin/env python

"""Server run file.

Run by './server.py'
Access properties as 'config.property'
"""

import datetime
from flask import Flask, send_file
from picamera import PiCamera, PiCameraError
from io import BytesIO
import config
import utils


app = Flask(__name__)


@app.route('/click')
def click():

    print('click!')
    
    # Create BytesIO stream for image capture
    image_stream = BytesIO()

    # Configure camera
    camera = PiCamera()
    camera.resolution = config.image_resolution

    # Add metadata
    camera.exif_tags['IFD0.Copyright'] = config.exif_copyright
    camera.exif_tags['EXIF.UserComment'] = 'Created at {}'.format(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))


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
