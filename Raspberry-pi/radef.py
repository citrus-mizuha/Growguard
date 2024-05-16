import time
import sys
import numpy as np
from pynput import keyboard
import subprocess
import os

def timestamp():
    return time.strftime('%Y/%m/%d %H:%M:%S')

def py_v():
    return sys.version

def sigmoid(x):
    return 1/(1+np.exp(-x))

