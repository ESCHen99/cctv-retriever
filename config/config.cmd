@ECHO off

ECHO Holaa
rem %1:cam %2:bitmask %3:ini %4:end
ECHO %2 > .\config\cam%1\config
ECHO %3 %4 > .\config\ini_end_time
ECHO %DATE% %TIME% bitmask %2  schedule %3 %4>> .\config\cam%1\log 

