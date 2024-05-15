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
system = platform.system()
machine = platform.machine()
conda_linux_rasp = "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh"
conda_linux_x86 = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh"
conda_linux_arm64 = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-aarch64.sh"  # AWS Graviton2/ARM64
conda_linux_special = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-s390x.sh"  # Linux on IBM Z & LinuxONE
conda_macos_arm64 = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-MacOSX-arm64.sh"
conda_macos_x86 = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-MacOSX-x86_64.sh"


def conda_set():
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


def conda_install():
    if system == "Linux":
        if machine == "x86_64":
            conda_url = conda_linux_x86
        elif machine == "aarch64":
            if "raspberrypi" in platform.uname().version:
                conda_url = conda_linux_rasp
            else:
                conda_url = conda_linux_arm64
        elif machine == "s390x":
            conda_url = conda_linux_special
        else:
            conda_url = None
    elif system == "Darwin":
        if machine == "x86_64":
            conda_url = conda_macos_x86
        elif machine == "arm64":
            conda_url = conda_macos_arm64
        else:
            conda_url = None
    else:
        conda_url = None

    if conda_url:
        print(f"It will be install conda. Ver." + system + machine)
        time.sleep(10)
        os.system(f"curl {conda_url} -o conda.sh")
        os.system("bash conda.sh")
    else:
        print("No suitable Conda installer found for your system.")


print("\nOS Type : " + system)
print("Machine Type : " + machine + "\n")
# Windows OSの場合のインストール
if system.lower() in ["windows", "windows os"]:
    if os.system("conda") == 0:
        conda_set()
    else:
        while True:
            agree_condainstall = input("Do you want to install conda to this WindowsPC? (y/n)")
            if agree_condainstall.lower() in ["y", "yes"]:
                print("Now, it will be install...")
                os.system("cd")
                os.system("curl https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Windows-x86_64.exe -o conda.exe")
                os.system("conda.exe")
                break
            if agree_condainstall.lower() in ["n", "no"]:
                while True:
                    pyvenv = input("It will make a env class. name=plant Agree? (y/n)")
                    if pyvenv.lower() in ["y", "yes"]:
                        os.system(r"\env\bin\activate")
                        os.system("pip install -r pip_env.txt")
                        print("pip install was end.")
                        break
                    if pyvenv.lower() in ["n", "no"]:
                        print("OK. This process will end.")
                        os.system("pip install -r pip_env.txt")
                        print("pip install was end.")
                        break
# 他のOSの場合
else:
    if conda_w == 0:
        conda_set()
    else:
        while True:
            print("Don't you want to install conda? We're recommend conda env.")
            agree_conda = input("Do you want to install conda? (y/n) ")
            if agree_conda.lower() in ["y", "yes"]:
                conda_install()
                conda_set()
                break
            if agree_conda.lower() in ["n", "no"]:
                while True:
                    agree_pyvenv = input("It will make a env class. name=plant Agree? (y/n)")
                    if agree_pyvenv.lower() in ["y", "yes"]:
                        os.system("source /env/bin/activate")
                        os.system("pip install -r pip_env.txt")
                        print("pip install was end.")
                        break

end = time.perf_counter()
print("Process End. \ntime taken : " + '{:.2f}'.format((end - start) / 60) + " m")
