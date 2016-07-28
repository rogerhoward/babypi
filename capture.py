#!/usr/bin/env python
from picamera import PiCamera
from time import sleep
import datetime, os

def stamped_name(base_filename, fmt='%Y-%m-%d-%H-%M-%S_{base}'):
    return datetime.datetime.now().strftime(fmt).format(base=base_filename)



print('welcome')

print('camera initializing...')
camera = PiCamera()
camera.resolution = (2592, 1944)
print('camera initialization complete...')

print('camera capturing...')
image_file = os.path.join('/home/pi/', stamped_name('image.jpg'))
camera.capture(image_file)
print('camera capture complete...')


# print('camera recording...')
# camera.start_recording('/home/pi/video.h264')
# sleep(10)
# camera.stop_recording()
# print('camera recording complete...')