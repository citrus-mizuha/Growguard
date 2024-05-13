import os
import time
import subprocess
import platform

start = time.perf_counter()
os.system("pip install -U pip")
conda_w = os.system("hash conda")
osx=("macOS","Ubuntu", "CentOS", "Unknown")
windowss=("Windows")

def os_type():
    system = platform.system()
    if system == "Darwin":
        return "macOS"
    elif system == "Linux":
        distribution = platform.linux_distribution()
        if "Ubuntu" in distribution:
            return "Ubuntu"
        elif "CentOS" in distribution:
            return "CentOS"
        elif "Raspbian" in distribution:
            return "Raspberry Pi OS"
        else:
            return "Unknown Linux Distribution"
    elif system == "Windows":
        return "Windows"
    else:
        return "Unknown"

os_type=os_type()

print("\nOS Type:", os_type+"\n")
if os_type in osx:
    if conda_w == 0:
        os.system("conda update --all")
        os.system("conda update -n base conda")
        while True:
            conda_plant = subprocess.check_output(["conda", "env", "list"]).decode("utf-8")
            if "plant" in conda_plant:
                os.system("conda activate plant")
                os.system("conda install -n plant --file conda_env.txt")
                os.system("conda update --all")
                break
            else:
                while True:
                    if input("It will make new env. name=plant Agree? (y/n)")=="y":
                        os.system("conda env create -f=conda_env.yml")
                        os.system("conda activate plant")
                        os.system("conda update --all")
                        break
    else:
        while True:
            pyvenv = input("It will make a env class. name=plant Agree? (y/n)")
            if pyvenv == "y":
                os.system("source /env/bin/activate")
                os.system("pip install -r pip_env.txt")
                print("pip install was end.")
                break
if os_type in windowss:
    if os.system("conda")==0:
        os.system("conda update --all")
        os.system("conda update -n base conda")
        while True:
            conda_plant = subprocess.check_output(["conda", "env", "list"]).decode("utf-8")
            if "plant" in conda_plant:
                os.system("conda activate plant")
                os.system("conda install -n plant --file conda_env.txt")
                os.system("conda update --all")
                break
            else:
                while True:
                    if input("It will make new env. name=plant Agree? (y/n)") == "y":
                        os.system("conda env create -f=conda_env.yml")
                        os.system("conda activate plant")
                        os.system("conda update --all")
                        break
    else:
        while True:
            pyvenv = input("It will make a env class. name=plant Agree? (y/n)")
            if pyvenv == "y":
                os.system("\env\bin\activate")
                os.system("pip install -r pip_env.txt")
                print("pip install was end.")
                break
end = time.perf_counter()
print("Process End. \ntime taken : " + '{:.2f}'.format((end - start) / 60) + " m")
