# ScreenInTheBottle
Useful link:
https://github.com/DaradiciLevente/ILI9488-on-Raspberry-Pi-Zero-2W-with-moOde-Audio
https://bytesnbits.co.uk/retropie-raspberry-pi-0-spi-lcd/

## Step 1
Download raspberrypi os lite 32-bit to the microcontroller, if you don't have

## Step 2
```bash
sudo nano /boot/firmware/config.txt
```
Write the end of config file these commands
```bash
# Force HDMI output, even if the cable is not plugged
hdmi_force_hotplug=1
# Customized resolution set
hdmi_group=2
hdmi_mode=87

# set resolution
hdmi_cvt=480 320 60 1 0 0 0

# turn off the oversizing, to avoid black borders
disable_overscan=1
```
Comment this line `dtoverlay-vc4-kms-v3d`
Reboot the system to apply settings

## Step 3
```bash
sudo raspi-config
```
Interface Options -> SPI -> Enable

## Step 4
To use `upload_to_pi.bat` without password follow commands bellow on your computer
#### Commands on your computer:
Generate a key on your computer
```bash
ssh-keygen -t rsa
```
The created key will be here: C:\Users\\'username\'\\.ssh\id_rsa

In the user folder create an ssh folder to the raspberry pi
```bash
ssh username@host "mkdir -p ~/.ssh"
```
Send key to the raspberry with this command
```bash
type C:\Users\'username'\.ssh\id_rsa.pub | ssh username@host "cat >> ~/.ssh/authorized_keys"
```
Edit host in `upload_to_pi.bat` file and click to run, the program will copy to the raspberry pi

## Step 5
update istaller, download git and cmake
download fbcp-ili9341 driver
```bash
sudo apt update
sudo apt install git cmake
sudo git clone https://github.com/juj/fbcp-ili9341.git
```

## Step 6
It is necessary to run make process
```bash
sudo apt install libraspberrypi-dev
```

## Step 7
Run this command
```bash
chmod +x build.sh
sudo ./build.sh
```

## Step 8
Stay in the build folder, rename fbcp-ili9341 to fbcp and copy to /usr/local/bin/fbcp so you can see it from anywhere in the system
```bash
 sudo cp fbcp-ili9341 /usr/local/bin/fbcp
```