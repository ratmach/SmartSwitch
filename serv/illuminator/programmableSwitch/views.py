from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import serial
import time

ser = serial.Serial("COM4")
statuses = ["checked","checked","checked","checked"]
def index(request):
	return render_to_response("index.html",{'user':'rati','names':
	[{"name":"p1","text":"charger","status":statuses[0]}
	,{"name":"p3","text":"lamp","status":statuses[2]}
	,{"name":"p2","text":"speaker","status":statuses[1]}
	,{"name":"p4","text":"nuclear plant","status":statuses[3]}]});
	
def params(request):
	inp = []
	if('p1' in request.GET):
		statuses[0]="checked";
		inp.append("01")
	else:
		statuses[0]="";
		inp.append("00")
		
	if('p2' in request.GET):
		statuses[1]="checked";
		inp.append("11")
	else:
		statuses[1]="";
		inp.append("10")
		
	if('p3' in request.GET):
		statuses[2]="checked";
		inp.append("21")
	else:
		statuses[2]="";
		inp.append("20")
		
	if('p4' in request.GET):
		statuses[3]="checked";
		inp.append("31")
	else:
		statuses[3]="";
		inp.append("30")
		
	for i in range(0,4):
		time.sleep(2);
		ser.write((inp[i]).encode())

		time.sleep(1)
		out = ""
		while ser.inWaiting() > 0:
			print(ser.read())

		if out != '':
			print(">>" + out)
			
	return index(request);