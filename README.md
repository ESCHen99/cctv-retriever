# cctv-retriever
## Summary
A CCTV software program to plan daily schedule recordings, download a period of these recordings and keep track of the alarms.
## FS
	Alarm 
	      |
          DDMMYY
                |
                HHMMSS

	Config
	      |
	       CAM #

	Records
        |
        DDMMYY
              |
              HHMMSS

	Tmp – As the name suggest is a temporal folder.

## Code
### HTTP Server Code
server_express.js – Send files via http, get info and manage schedule.
### main code
main.py
### auxiliary batch scripts
- cut.cmd – Concatenate videos of minutes before the alarm
- config.cmd – Arranges the configuration of the cameras

## API 
	BASE URL 
		http://server:port/
		  Request URL
			/request/?cam=X&day=DDMMYY&alarm=HHMMSS
		  Info URL
			/info
		  Scheduler
		      	/schedule/?cam=X&schedule=bbbbbbb&ini:HH:MM&end=HH:MM

## Installation
* Python - https://www.python.org/downloads/
* Node.JS - https://nodejs.org/en/download/
* Express.js
```
$ npm install express
```
* filter-files
```
$ npm i filter-files
```
* child_process
```
$ npm i childprocess
```
* execSync
```
$ npm install execSync
```

## Version 
1.0.0
### Implemented
- Scheduler
- Request
