import os
import time
import subprocess

start = time.perf_counter()
conda_w = os.system("hash conda")
if conda_w == 0:
    while True:
        conda_plant = subprocess.check_output(["conda", "env", "list"]).decode("utf-8")
        if "plant" in conda_plant:
            os.system("conda install -n plant --file conda_env.txt")
            break
        else:
            while True:
                if input("It will make new env. name=plant Agree? (y/n)")=="y":
                    os.system("conda env create -f=conda_env.yml")
                    break
    os.system("conda activate plant")
else:
    while True:
        pyvenv=input("It will make a env class. name=plant Agree? (y/n)")
        if pyvenv=="y":
            os.system("source /env/bin/activate")
            os.system("pip install -r pip_env.txt")
            print("pip install was end.")
            break

end = time.perf_counter()
print("Process End. \ntime taken : " + '{:.2f}'.format((end - start) / 60) + " m")
