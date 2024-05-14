import os
import time
import subprocess
import platform

# This is a management device's setup code.
# If you want to set up on client device, Please execute c-setup.py.

start = time.perf_counter()
os.system("pip install -U pip")
conda_w = os.system("hash conda")
osx = ("macOS", "Ubuntu", "CentOS", "Unknown")
windows = "Windows"

def conda_s():
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
                conda = input("It will make new env. name=plant Agree? (y/n)")
                if conda.lower() in ["y", "yes"]:
                    os.system("conda env create -f=conda_env.yml")
                    os.system("conda activate plant")
                    os.system("conda update --all")
                    break


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
            return "Unknown"
    elif system == "Windows":
        return "Windows"
    else:
        return "Unknown"


os_type = os_type()

print("\nOS Type:", os_type + "\n")
if os_type.lower() in ["macos", "centos", "ubuntu", "unknown"]:
    if conda_w == 0:
        conda_s()
    else:
        while True:
            pyvenv = input("It will make a env class. name=plant Agree? (y/n)")
            if pyvenv.lower() in ["y", "yes"]:
                os.system("source /env/bin/activate")
                os.system("pip install -r pip_env.txt")
                print("pip install was end.")
                break
if os_type.lower() in ["windows"]:
    if os.system("conda") == 0:
        conda_s()
    else:
        while True:
            pyvenv = input("It will make a env class. name=plant Agree? (y/n)")
            if pyvenv.lower() in ["y", "yes"]:
                os.system(r"\env\bin\activate")
                os.system("pip install -r pip_env.txt")
                print("pip install was end.")
                break
if os_type.lower() in ["raspbian"]:
    raspbian = input(r"It will be build in This Device. Do you want to build? (y/n)")
    # (Both client system and manage system will set up in this Device.) をどう追加するか
    if raspbian.lower() in ["y", "yes"]:
        print(r"Starting.... ")
        time.sleep(10)
        # また今度書く
end = time.perf_counter()
print("Process End. \ntime taken : " + '{:.2f}'.format((end - start) / 60) + " m")
