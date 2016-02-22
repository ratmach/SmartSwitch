from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from programmableSwitch.models import user, points
import serial
import string
import time
import random

accessLog = []

ser = serial.Serial("COM4")
statuses = ["checked","checked","checked","checked"]

def startServer(request): 
	statuses = ["checked","checked","checked","checked"]
	return HttpResponse("done")
	
def stopServer(request):
	ser.close()

def register(request):
	if("username" in request.GET and "password" in request.GET and "type" in request.GET):
		tmp = generateUID(32);
		while(len(user.objects.filter(UID = tmp)) > 0):
			tmp = generateUID(32);
		u = user.objects.create(UID=tmp,username=request.GET["username"],password=request.GET["password"],type=request.GET["type"])
		return HttpResponse(tmp)
	return HttpResponse("");
	
def generateUID(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
	
def auth(request):
	if("username" in request.POST and "password" in request.POST):
		t = user.objects.filter(username = request.POST["username"], password = request.POST["password"]);
		if(len(t) > 0):
			return mIndex(request,t[0]);
	return render(request, 'auth.html', status = 403);
	
def logout(request):
	response = index(request);
	response.set_cookie("UID","");
	return response;
	
def registerPoints(request):
	points.objects.create(name="1",watt=0.0, pID=0,icon="default.png",state=False,type=0);
	points.objects.create(name="2",watt=0.0, pID=1,icon="default.png",state=False,type=0);
	points.objects.create(name="3",watt=0.0, pID=2,icon="default.png",state=False,type=0);
	points.objects.create(name="4",watt=0.0, pID=3,icon="default.png",state=False,type=0);
	return HttpResponse("done")

def mIndex(request,user):
	p = points.objects.all();
	tmp = render_to_response("index.html",{'user':user,'points':p});
	tmp.set_cookie('UID',user.UID)
	return tmp
	
def index(request):
	if("UID" in request.COOKIES):
		u = user.objects.filter(UID=request.COOKIES["UID"])
		if(len(u) > 0):
			p = points.objects.filter(type__lte = u[0].type)
			return render_to_response("index.html",{'user':u[0],'points':p})
	return auth(request)

def changeStates(request):
	outp = ""
	for key in request.GET.keys():
		points.objects.filter(pID = key).update(state=(request.GET[key] == "0"))
		p = points.objects.get(pID = key);
		outp+=key + str(p.state) + "\n"
	updateBoard()
	return HttpResponse(outp);
	
def displayLog(request):
	a = points.objects.get(pID=0)
	a.type=100;
	a.save();
	return index(request);
	
def updateBoard():
	p = points.objects.all();
	for i in range(0,len(p)):
		time.sleep(2);
		if(p[i].state):
			print(str(p[i].pID) + "1");
			ser.write((str(p[i].pID) + "1").encode())
		else:
			print(str(p[i].pID) + "0");
			ser.write((str(p[i].pID) + "0").encode())
		
		out = ""
		while ser.inWaiting() > 0:
			print(ser.read())

		if out != '':
			print(">>" + out)
updateBoard()