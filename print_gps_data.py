#Python test file to print gps data
import serial
import time

ser = serial.Serial("/dev/ttyACM0")
timestamp = time.strftime("%y%m%d_%H%M%S")
filename = "gps_" + timestamp + ".txt"
print("file created with filename" + filename)

gps_file = open(filename, "a+")

while 1:
    line = ser.readline()
    splited = line.split(b',')
    if (splited[0] == b'$GPGGA'):
        parsed_data = "lat :, " + splited[2] + " , log :, " + splited[4] + ",\n"
        gps_file.write(parsed_data)
        print(parsed_data) 
