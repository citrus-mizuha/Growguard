import os
import subprocess as sub
import time
import radef
import pynput

print(radef.py_v())
print("This process will setup Raspberry pi. So, please execute in Raspberry pi. "
      "If you want to setup other OS PC for management, please press the esc key.")
if pynput.is_pressed("escape"):
    sub.run(["python3", "m-setup.py"])
    exit()
time.sleep(5)
print("Hello")