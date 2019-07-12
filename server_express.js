const express = require('express');
const filter = require('filter-files');
const spawn = ('child_process');
const execSync = require('child_process').execSync;
var path = require('path');


var app = express();

app.get('/', function(req,res)
{
	res.sendFile(path.join(__dirname + '/html/index.html'));
});

app.get('/request', (req, res) => { 
		var cam = req.query.cam;
		var day = req.query.day;
		var alarm=req.query.alarm;
		if (cam == undefined || day == undefined || alarm == undefined){
				res.send("cam, day or alarm unspecified")
		}
		var path = `./records/cam${cam}/${day}`;
		

		var current = undefined;
		var ant = undefined;
		
		var files = filter.sync(path, function(fp) {
							if(fp<alarm){
								ant = current;
								current = fp;
								return false;
							}
							return true;
		});
				
		/* CRIDAR SCRIPT CAM 1 SYNC*/
		execSync(`cut.cmd ${cam} ${day} ${alarm} ${ant} ${current}`);
		
		var filePath=`./alarm/${day}/${alarm}.avi`;
		console.log(filePath);
		
		/* DOWNLOAD  */
		res.download(filePath, alarm+'.avi', (err) => {
				if(err){
					res.send('SERVER ERROR contact TAVIL');
					console.log(err);
				}
			//	else res.send('done');
			});
});

app.get('/info', (req, res) => {res.send('Show log files of cameras')});

app.get('/schedule', (req, res) => {
		var cam = req.query.cam;
		var bitmask = req.query.schedule;
		var ini = req.query.ini;
		var end = req.query.end;
		execSync(`config\\config.cmd ${cam} ${bitmask} ${ini} ${end}`);
		res.send('Done!');
});


app.use(function(error, req, res, next) {
  // Will get here
  res.json({ message: error.message });
});


var server = app.listen(3030, () => {});
