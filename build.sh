#!/bin/bash
# This script builds the project with specific configurations for the ILI9488 display.

# entry in fbcp-ili9341 directory, because not allowed to copy directly from windows in this folder
cd fbcp-ili9341

sudo rm -rf build
echo -e "\e[31mBuild folder removed.\e[0m"
sudo mkdir build
cd build
pwd

sudo cmake .. \
  -DILI9488=ON \
  -DGPIO_TFT_DATA_CONTROL=24 \
  -DGPIO_TFT_RESET_PIN=25 \
  -DGPIO_TFT_BACKLIGHT=2 \
  -DSPI_BUS_CLOCK_DIVISOR=12 \
  -DUSE_DMA_TRANSFERS=ON \
  -DDMA_TX_CHANNEL=3 \
  -DDMA_RX_CHANNEL=1 \
  -DDISPLAY_CROPPED_INSTEAD_OF_SCALING=OFF \
  -DDISPLAY_BREAK_ASPECT_RATIO_WHEN_SCALING=ON \
  -DSHOW_DEBUG_INFO=OFF \
  -DSTATISTICS=0 \
  -DDISPLAY_SHOW_TEMPERATURE=OFF \
  -DDISPLAY_ROTATE_180_DEGREE=ON \
  -DDISPLAY_SWAP_XY_IN_SOFTWARE=OFF

echo -e "\e[32mCMake configuration completed.\e[0m"

sudo make -j
echo -e "\e[32mBuild completed successfully.\e[0m"
