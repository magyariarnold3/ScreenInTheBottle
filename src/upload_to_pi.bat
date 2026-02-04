@echo off
set RPI_HOST=pi@192.168.0.112
set RPI_PATH=/home/pi/ScreenInTheBottle
set LOCAL_PATH=%cd%

scp -r "%LOCAL_PATH%\*" %RPI_HOST%:%RPI_PATH%