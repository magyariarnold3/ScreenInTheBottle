#!/bin/bash
# Only if you use RealVNC Viewer
# This code setup wayvnc server on current IP address and 5902 port
# Anyone can connect

if [ -z "$WAYLAND_DISPLAY" ]
then
    WLR_BACKENDS=headless cage -- "$0"

    # When the cage closes, the script is end
    exit 0
fi 

# 1. Start the VNC server in the background(&) 
wayvnc 0.0.0.0 5902 &

# 2. Wait for system startup
sleep 4

# 3. Set the resolution for headless mode
wlr-randr --output HEADLESS-1 --custom-mode 480x640

# 4. Start the zatura
zathura -c /home/pi/ScreenInTheBottle /home/pi/Haskell.pdf