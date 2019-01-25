#Python test file to print gps data
import serial
import time
import re

ser = serial.Serial("/dev/ttyACM0")
timestamp = time.strftime("%y%m%d_%H%M%S")
filename = "gps_" + timestamp + ".csv"
print("file created with filename" + filename)

gps_file = open(filename, "a+")

while 1:
    line = ser.readline()
    splited = line.split(b',')
    if (splited[0] == b'$GPGGA'):
        if not (splited[2] is None):
            #Eg, 12319.943281
            d, m = re.match(r'^(\d+)(\d\d\.\d+)$', splited[2]).groups()    # d=123 m=19.943281
            lat = float(d) + float(m) / 60                                 # lat = 123.33238801666667
            d, m = re.match(r'^(\d+)(\d\d\.\d+)$', splited[4]).groups()
            lon = float(d) + float(m) / 60
            parsed_data = lat + "," + lon + "\n"
            gps_file.write(parsed_data)
            print(parsed_data)
