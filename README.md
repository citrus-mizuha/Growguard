# GrowGuard
## Developers
| Name                                              | position            |
|---------------------------------------------------|---------------------|
| [citrus-mizuha](https://github.com/citrus-mizuha) | PM(project manager) |
| [citrus-soke](https://github.com/citrus-soke)     | Main Developer      |
## About
### Responsibility
We do not assume any responsibility for the use of our service.([in detail](LICENSE))
### How to install
- If you use conda : 
```shell
$ conda create -n plant python=3.12 #Although it is not necessary to create a new environment, we recommend creating a new environment.
$ conda activate plant
$ conda install opencv numpy matplotlib & pip install influxdb influxdb-client
# if you use MacOS : 
$ brew install opencv
```
- Else :
```shell
$ python3 -m venv plant
  # if you using MacOS or LinuxOS : 
    $ source plant/bin/activate
  # if you using WindowsOS : 
    $ .\plant\bin\activate
$ pip install opencv numpy matplotlib influxdb influxdb-client
```
in the either case :
```python
import cv2
import influxdb as influx
import influxdb_client as client
print(cv2.__version__)
print(influx.__version__)
print(client.__version__)
```
If a number such as "4.9.0" is returned, the installation is complete. If you encounter an error, please check it yourself.
### How to use

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

## 