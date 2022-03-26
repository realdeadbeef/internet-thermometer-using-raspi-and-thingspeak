import httplib
import urllib
import time
import os
import glob

key = "ABCEDFG1234567"  # Put your API Key here

def thermometer():
    while True:
        #########################################################################################################
        # Initialize the GPIO Pins
        os.system('modprobe w1-gpio')  # Turns on the GPIO module
        os.system('modprobe w1-therm')  # Turns on the Temperature module

        # Finds the correct device file that holds the temperature data
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        device_file = device_folder + '/w1_slave'

        # A function that reads the sensors data
        def read_temp_raw():
            with open(device_file, 'r') as f:
                lines = f.readlines() # Returns the text
            return lines
        # Convert the value of the sensor into a temperature
        def read_temp():
            lines = read_temp_raw()  # Read the temperature 'device file'
            # While the first line does not contain 'YES', wait for 0.2s
            # and then read the device file again.
            while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
        # Look for the position of the '=' in the second line of the
            # device file.
            equals_pos = lines[1].find('t=')
            # If the '=' is found, convert the rest of the line after the
            # '=' into degrees Celsius, then degrees Fahrenheit
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                return float(temp_string) / 1000.0

        #########################################################################################################
        #Calculate temperature of thermometer in Degrees C
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get temp
        params = urllib.urlencode({'field1': (read_temp()), 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print read_temp
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break
if __name__ == "__main__":
        while True:
                thermometer()
