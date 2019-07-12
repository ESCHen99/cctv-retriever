import threading
import os
import schedule
import time

file = open("./config/ini_end_time")
time = file.read()
hIni = time[0]+time[1];
mIni = time[3]+time[4];
file.close();

start = hIni+':'+mIni;

def cam1():
	os.system('python ./config/cam1/cam1.py')

def cam2():
	os.system('python ./config/cam2/cam2.py')         

def cam3():
	os.system('python ./config/cam3/cam3.py')   

def cam4():
	os.system('python ./config/cam4/cam4.py') 
	
def cam(camN):
	os.system('python ./config/cam.py cam'+str(camN))                         
# Process for CAM1
# Process for CAM2
# Process for CAM3
# Process for CAM4

def main():
	threads=[]

	t1 = threading.Thread(target=cam1)
	threads.append(t1)
	t1.start()

	t2 = threading.Thread(target=cam2)
	threads.append(t2)
	t2.start()

	t3 = threading.Thread(target=cam3)
	threads.append(t3)
	t3.start()

	t4 = threading.Thread(target=cam4)
	threads.append(t4)
	t4.start()

def main2():
	threads=[]
	for i in range(4):
		t = threading.Thread(target = cam, args=(i,))
		threads.append(t)
		t.start()

schedule.every().day.at(start).do(main2);


while True:
	schedule.run_pending();
