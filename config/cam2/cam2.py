import sys
import os
import datetime

file = open("./config/ini_end_time")
time = file.read()
hIni = time[0]+time[1];
mIni = time[3]+time[4];
hEnd = time[6]+time[7];
mEnd = time[9]+time[10];
time = (int(hEnd)-int(hIni))*3600 + (int(mEnd)-int(mIni))*60

credentials = open('./config/cam2/credentials')
bitmask = open('./config/cam2/config')

credentialsStr = credentials.read();
bitmaskStr = bitmask.read();

credentials.close();
bitmask.close();

W = datetime.date.today().weekday();
print(bitmaskStr[W]);
if bitmaskStr[W]=='1':
	DD = datetime.date.today().day;
	if DD < 10: 
		DD = '0' + str(DD);
	else:
		DD = str(DD);


	MM = datetime.date.today().month;

	if MM<10:
		MM = '0' + str(MM);
	else:
		MM = str(MM);

	YY = str(datetime.date.today().year%100);

	day = DD + MM + YY

	if not os.path.isdir('./records/cam2/'+day):
		os.system('mkdir '+ '.\\records\\cam2\\' +day);

	print(credentialsStr);
	myCmd = 'ffmpeg  -rtsp_transport tcp -i ' + '"' + credentialsStr +'"' + ' -f segment -segment_time 120 -segment_format avi -reset_timestamps 1'+ ' -t ' + str(time) +' -strftime 1 -c copy -map 0 .\\records\\cam2\\' + day + '\\%H%M%S.avi'
	os.system(myCmd)
else :
	print('Today no job');

