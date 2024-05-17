import time
import sys
import numpy as np
from pynput import keyboard
import subprocess
import os

def timestamp(x):
    if x == "ymd":
        return time.strftime("%Y/%m/%d")
    else:
        return time.strftime('%Y/%m/%d %H:%M:%S')

def py_v():
    return sys.version

def sigmoid(x):
    return 1/(1+np.exp(-x))

def pip_update():
    pipchecker_pip_review = subprocess.check_output(["pip", "list", "|", "grep","pip"]).decode("utf-8")
    if pipchecker_pip_review.lower() not in ["pip-review"]:
        os.system("pip install pip-review")
        os.system("pip-review --auto")
    else:
        os.system("pip-review --auto")


def repository_update():
    subprocess.run(["git","pull"])
    print("Repository was updated.")
