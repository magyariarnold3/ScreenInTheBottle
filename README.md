# ScreenInTheBottle

## Step 1
Download raspberrypi os lite 32-bit to the microcontroller, if you don't have

## Step 2
    sudo nano /boot/firmware/config.txt
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

## Step 3
    sudo raspi-config
Interface Options -> SPI -> Enable

## Step 4
update istaller, download git and cmake
download fbcp-ili9341 driver
```bash
sudo apt update
sudo apt install git cmake
sudo git clone https://github.com/juj/fbcp-ili9341.git
```

## Step 5
Run this command

    sudo ./build.sh