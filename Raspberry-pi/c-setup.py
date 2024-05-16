import os
import subprocess
import time
import radef

print(radef.py_v())
print("This process will setup Raspberry pi. So, please execute in Raspberry pi. \n"
      "If you want to setup other OS PC for management, please write 'management' or 'manage'.\n"
      "And if you want to execute this program, please write 'y' or 'yes'")
process_continue = input("Write here : ")
if process_continue.lower() in ["management", "manage"]:
    subprocess.run(["python3", "m-setup.py"])
if process_continue.lower() in ["y", "yes"]:
    print("Ok, this program will continue")
else :
    print("Please execute one more time.")
    exit()

