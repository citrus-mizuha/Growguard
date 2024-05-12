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
   And then, Please run the code below
```python
import cv2
import influxdb as influx
import influxdb_client as client
print(cv2.__version__)
print(influx.__version__)
print(client.__version__)
# If a number such as "4.9.0" is returned, the installation is complete. If you encounter an error, please check it yourself.
```
- Else : 
### How to use
