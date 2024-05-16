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
conda_linux_x86 = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh"  # x86 LinuxOS
conda_linux_arm64 = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-aarch64.sh"  # AWS Graviton2/ARM64
conda_linux_special = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-s390x.sh"  # Linux onIBM Z & LinuxONE
conda_macos_arm64 = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-MacOSX-arm64.sh"
conda_macos_x86 = "https://repo.anaconda.com/archive/Anaconda3-2024.02-1-MacOSX-x86_64.sh"


def conda_set():
    os.system("conda update --all")
    os.system("conda update -n base conda")
    while True:
        conda_plant = subprocess.check_output(["conda", "env", "list"]).decode("utf-8")
        if "plant" in conda_plant:
            conda_prefix = subprocess.check_output(['conda', 'info', '--base']).decode('utf-8').strip()
            activate_script = os.path.join(conda_prefix, 'etc', 'profile.d', 'conda.sh')
            command = (f"source {activate_script} && conda activate plant && "
                       f"conda install -n plant --file conda_env.txt && conda update --all")
            os.system(f"bash -c '{command}'")
            break
        else:
            while True:
                conda = input("It will make new env. name=plant Agree? (y/n)")
                if conda.lower() in ["y", "yes"]:
                    os.system("conda env create -f=conda_env.yml")
                    # Activate the newly created environment
                    conda_prefix = subprocess.check_output(['conda', 'info', '--base']).decode('utf-8').strip()
                    activate_script = os.path.join(conda_prefix, 'etc', 'profile.d', 'conda.sh')
                    command = f"source {activate_script} && conda activate plant && conda update --all"
                    os.system(f"bash -c '{command}'")
                    break


def conda_install():
    if system == "Linux":
        if machine == "x86_64":
            conda_url = conda_linux_x86
        elif machine == "aarch64":
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


def finish():
    end = time.perf_counter()
    print("Process End. \ntime taken : " + '{:.2f}'.format((end - start) / 60) + " m")


print("\nOS Type : " + system)
print("Machine Type : " + machine + "\n")
subprocess.run(["python3", "-m", "pip", "install", "SomePackage"])

while True:
    ok = input('''
Are you using a device other than Raspberry pi?
If you are using a Raspberry pi, enter "n" If you are using another OS, enter"y" : ''')
    if ok.lower() in ["y", "yes"]:
        print("Ok, It will be run.")
        break
    if ok.lower() in ["n", "no"]:
        while True:
            check = input("If you using Raspberry pi, Please write 'Raspberrypi' here. : ")
            if check.lower() in ["raspberrypi"]:
                print("Ok, It will run the another setup code.")
                subprocess.run(["python3", "ra-setup.py"])
                finish()
                exit()
            else:
                print("Please execute one more time.")
                finish()
                exit()

# Windows OSの場合のインストール
if system.lower() in ["windows", "windows os"]:
    if os.system("conda") == 0:
        conda_set()
    else:
        while True:
            agr_conda_install = input("Do you want to install conda to this WindowsPC? (y/n)")
            if agr_conda_install.lower() in ["y", "yes"]:
                print("Now, it will be install...")
                os.system("cd")
                os.system("curl https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Windows-x86_64.exe -o conda.exe")
                os.system("conda.exe")
                break
            if agr_conda_install.lower() in ["n", "no"]:
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

finish()
