# GrowGuard
[![image](https://img.shields.io/pypi/v/pipenv.svg)](https://python.org/pypi/pipenv)
[![image](https://img.shields.io/pypi/l/pipenv.svg)](https://python.org/pypi/pipenv)
[![image](https://img.shields.io/pypi/pyversions/pipenv.svg)](https://python.org/pypi/pipenv)
[![Qodana](https://github.com/citrus-mizuha/growguard/actions/workflows/qodana_code_quality.yml/badge.svg)](https://github.com/citrus-mizuha/growguard/actions/workflows/qodana_code_quality.yml)
-------------------------------------------------
## Developers
| Name                                              | position            |
|---------------------------------------------------|---------------------|
| [citrus-mizuha](https://github.com/citrus-mizuha) | PM(project manager) |
| [citrus-soke](https://github.com/citrus-soke)     | Main Developer      |


## About
This project is developed by third-year junior high school students in Japan (at the start of the project)
We are developing a device with irrigation functions for plants, nutrient management functions, humidity control functions (and a function to control the air conditioner in the case of indoors), etc., and we are developing code that can achieve similar functions on the Raspberry pi, although it is one step lower in terms of performance.
(Please be assured that the part where money is involved is left to a trusted adult) (Donation is [here]())
In addition, we do not accept any responsibility related to this program and the device. Therefore, it is recommended to treat it as a watering machine for hobby plant cultivation.
For more information on the disclaimer, please see [here]()
## Compatible devices
### Compatible devices
- Raspberry pi 3 or 4 or 5
- Plant-guarder (original Device)
[Plant-guarder](https://example.com) is very cheap and stable Device (This is a dedicated device developed by mizuha.).
### Device settings and data management(Recommend environment)
- Raspberry pi (self)
- MacOS
- WindowsOS
- LinuxOS
If you use "Plant-guarder", you have to set by dedicated app.

## How to use
### How to setup
1. If you use Raspberry Pi :
   - If you use dedicated application : 
   Please open the GrowGuarder App. And, Please follow the guide. (you need a Wi-Fi environment to ssh environment.)

   - If you don't want to use dedicated application :
   Please execute like this on Raspberry pi.
        ```shell 
        cd Raspberry-pi & bash setup.sh #"bash setup.sh" = "./setup.sh" = ".\setup.sh"
        ```

2. If you use "grow-guarder" :
(You can use it without downloading the app, but downloading the app will make data management and setup easier.)

   - If you use dedicated application :
     Please open the GrowGuarder App. And, Please follow the guide.
   - If you don't want to use dedicated application :
     Please connect Plant-guarder to ManagementPC by usb.
      ```shell
      cd grow-guarder & bash webui.sh #.\webui.sh (Windows OS)
      ```
     Please access [localhost:728](https://localhost:728). And, please follow the guide. 
### How to manage datas and How to change setting (parameter)
- If you use Raspberry pi : 

  That data is saved on Raspberry pi's Influxdb. So, you can see in the Influxdb's SQL and You can see like [that]() file.
  at `growguard/Raspberry-pi/saced-data/year-month.csv` Please check.
- If you use grow-guarder : 

    If you have set up Wi-Fi on GrowGuarder, you can check the data on the grow-guarder app.
    If you have not set up Wifi, connect Grow-guarder with a wire and open the grow-guarder app, or set up Bluetooth in advance, go near GrowGuarder and open the grow-guarder app, Once connected, you can view the data.
### 


## Responsibility
We do not assume any responsibility for the use of our service.([in detail](LICENSE))

