@ECHO OFF

echo file '.\records\cam%1\%2\%4' > .\tmp\myfiles.txt
echo file '.\records\cam%1\%2\%5' >> .\tmp\myfiles.txt

IF NOT EXIST .\alarm\%2 mkdir .\alarm\%2
ffmpeg -safe 0 -f concat -i .\tmp\myfiles.txt -c copy .\alarm\%2\%3.avi -y
DEL .\tmp\myfiles.txt

ECHO DONE!
