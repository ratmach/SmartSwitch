import serial
import time

ser = serial.Serial("COM4")

print (ser.portstr)
time.sleep(3);
while 1:
	inp = input(">> ")
	if (inp == "exit"):
		break
	ser.write((inp).encode())

	time.sleep(1)
	out = ""
	while ser.inWaiting() > 0:
		print(ser.read())

	if out != '':
		print(">>" + out)
		
ser.close()