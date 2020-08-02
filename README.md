## Thingspeak
Go to https://thingspeak.com/ and hit "Get started for free". Create your account and then log in
* Press "New Channel".
* Give it a name, scroll to the bottom and click "Save channel".
* Click on "API Keys" at the top of the screen.
* Copy the write API key

## Initial Setup.
For this project you will need:
* A raspberry pi running raspbian buster lite
* A DS18B20 temperature sensor
* A breadboard
* Jumper leads
* 4.7k Resistor

## Wiring.
Note: this should be done while the pi is switched off

Look at "Wiring.png"	
## Setup (Code).
To setup this project, follow these commands in terminal

Before you can use any 1-wire devices, you must first tell the Raspberry Pi how to read them.

Type:
```
sudo nano /boot/config.txt
```
And then add the line to the bottom of the file:
```
dtoverlay=w1-gpio
```
Now press "CTRL+X" followed by "Y" and then "Enter"
Now reboot:
```
sudo reboot
```
Once the pi has rebooted, clone the repo:
```
git clone https://github.com/tm2007/internet-thermometer-using-raspi-and-thingspeak.git
```
Install pip3:
```
sudo apt install python3-pip
```
Install httplib2
```
sudo pip3 install httplib2
```
Install urllib3
```
sudo pip3 install urllib3
```
## Running the script.
Type:
```
sudo nano internet-thermometer-using-raspi-and-thingspeak/code.py
```
And look for the line: ```key = "ABCEDFG1234567"  # Put your API Key here``` And replace ABCEDFG1234567 with your API key.

Now press "CTRL+X" followed by "Y" and then "Enter"

And then to run the script:
```
python internet-thermometer-using-raspi-and-thingspeak/code.py
```
