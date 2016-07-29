#!/usr/bin/env python

"""Useful utilities.
import utils
Access functions like as utils.stamped_name()
"""

import datetime


def stamped_name(base_filename, fmt='%Y-%m-%d-%H-%M-%S_{base}'):
    return datetime.datetime.now().strftime(fmt).format(base=base_filename)
