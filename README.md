# ScreenInTheBottle

## fbcp-ili8488 driver configuration

Useful link:
https://github.com/DaradiciLevente/ILI9488-on-Raspberry-Pi-Zero-2W-with-moOde-Audio
https://bytesnbits.co.uk/retropie-raspberry-pi-0-spi-lcd/
https://www.youtube.com/watch?v=I41wIyXG8Bc

## Step 1

Download raspberrypi os Buster(Debian 10) lite 32-bit to the microcontroller, if you don't have

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

**Commands on your computer:**

Delete old keys associated with this IP address

```bash
ssh-keygen -R 'ip cim'
```

Generate a key on your computer
-t: type, used algorithm type

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

---

## DPI Screen

### PDF reader and controll

> **The operating system used**\
*Raspberry Pi OS Lite (32-bit)*\
*A port of Debian Trixie with no desktop environment*\
*Released: 2025-12-04*

### Step 1

* `cage` it is a kiosk
* `zathura` it is a pdf reader app
* `bluetooth` and `bluez` tools for controlling the shutter

```bash
sudo apt update && sudo apt install cage zathura bluetooth bluez
```

### Step 2

Use these commands if you don't have a physical screen and use VNC viewer

```bash
 WLR_BACKENDS=headless cage -- bash -c "wayvnc 0.0.0.0 5902 & sleep 4; wlr-randr --output HEADLESS-1 --custom-mode 480x640; zathura /home/pi/Haskell.pdf"
```

or run this start_gui.sh file

```bash
chmod +x start_gui.sh
./start_gui.sh
```

### Step 3

Connect shutter to the raspberry

```bash
sudo bluetoothctl
scan on
```

If the bluetooth is blocked

```bash
sudo rfkill unblock bluetooth
sudo systemctl restart bluetooth
sudo bluetoothctl
power on
scan on

pair XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX
```

### Step 4

```bash
sudo apt install wtype
# send a sapce key e.g
wtype -k space
```

## 🛒 Bill of Materials

Here is the list of components and tools required for the project.

| Component Name                | Quantity  | Price (approx.) | Link (Source)           | Note  |
| :---                          | :---:     | :---:           | :---                    | :---  |
| **Samsung INR18650-35E**      | 2         | 53 lei          | [Emag](<https://www.emag.ro/acumulator-samsung-inr18650-35e-3500mah-li-ion-3-7v-18-2x65-0mm-8a-cu-terminale-lipite-1865035est/pd/DFFTZHMBM/>) |
| **Ecran IPS, Waveshare, DPI, 2.8", 480x640, Pentru Raspberry Pi, Negru** | 1 | 192 lei | [Emag](<https://www.emag.ro/ecran-ips-waveshare-dpi-2-8-480x640-pentru-raspberry-pi-negru-2-8inchdpilcdwaveshare18628/pd/DZKXPRMBM/>) | |
| **SW6106 Power Bank Module**  | 1         | 29 lei          | [Aliexpress](<https://www.aliexpress.com/item/1005008855046067.html?spm=a2g0o.cart.0.0.489b38day5jejT&mp=1&pdp_npi=6%40dis%21RON%21RON%2029.04%21RON%2029.04%21%21RON%2029.04%21%21%21%402103917f17702903208743773ea87f%2112000046959051598%21ct%21RO%212914208444%21%211%210%21>) | |
| **Fast Blow PICO Resistance Fuse** | 5 | 16 lei | [Aliexpress](<https://www.aliexpress.com/item/33001001526.html?spm=a2g0o.cart.0.0.489b38day5jejT&mp=1&pdp_npi=6%40dis%21RON%21RON%2016.85%21RON%2016.72%21%21RON%2016.72%21%21%21%402103917f17702903208743773ea87f%2112000034045751913%21ct%21RO%212914208444%21%211%210%21>) | |
| **One Way Window Film, Mirror Effect** | 1 | 19 lei | [Aliexpress](<https://www.aliexpress.com/item/1005005240874660.html?spm=a2g0o.cart.0.0.489b38day5jejT&mp=1&pdp_npi=6%40dis%21RON%21RON%2059.44%21RON%2019.61%21%21RON%2019.41%21%21%21%402103917f17702903208743773ea87f%2112000032595915830%21ct%21RO%212914208444%21%211%210%21>) | |
| **Transparent Plexi Glass** | 1 | 30 lei | [Aliexpress](<https://www.aliexpress.com/item/32817321651.html?spm=a2g0o.cart.0.0.489b38day5jejT&mp=1&pdp_npi=6%40dis%21RON%21RON%2030.82%21RON%2030.82%21%21RON%2030.82%21%21%21%402103917f17702903208743773ea87f%2112000044393459801%21ct%21RO%212914208444%21%212%210%21>) |
| **Reed Switch Magnetic Switch Sensor** | 5 | 20 lei | [Aliexpress](<https://www.aliexpress.com/item/1005008194740665.html?spm=a2g0o.cart.0.0.489b38day5jejT&mp=1&pdp_npi=6%40dis%21RON%21RON%2020.69%21RON%2020.69%21%21RON%2020.69%21%21%21%402103917f17702903208743773ea87f%2112000044196159444%21ct%21RO%212914208444%21%212%210%21&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22pdpBusinessMode%22%3A%22retail%22%7D%7D>) | |
| **Neodium Magnet** | 2 | 26 lei | [Aliexpress](<https://www.aliexpress.com/p/shoppingcart/index.html?spm=a2g0o.best.header.1.33412c25LdAvTo>) | |