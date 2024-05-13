import numpy as np
import influxdb
import influxdb_client
import Adafruit_GPIO
import time
import sys

def timestamp():
    return time.strftime('%Y/%m/%d %H:%M:%S')

def py_v():
    return sys.version
