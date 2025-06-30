#!/bin/bash
# This script builds the project with specific configurations for the ILI9488 display.

# entry in fbcp-ili9341 directory, because not allowed to copy directly from windows in this folder
cd fbcp-ili9341

sudo rm -rf build
echo -e "\e[31Build folder removed.\e[0m"
sudo mkdir build

cmake .. \
  -DILI9488=ON \
  -DGPIO_TFT_DATA_CONTROL=24 \
  -DGPIO_TFT_RESET_PIN=25 \
  -DGPIO_TFT_BACKLIGHT=12 \
  -DDISPLAY_ROTATE_180_DEGREE=OFF \
  -DSPI_BUS_CLOCK_DIVISOR=12 \
  -DUSE_DMA_TRANSFERS=ON \
  -DDMA_TX_CHANNEL=3 \
  -DDMA_RX_CHANNEL=1 \
  -DDISPLAY_CROPPED_INSTEAD_OF_SCALING=ON \
  -DDISPLAY_BREAK_ASPECT_RATIO_WHEN_SCALING=ON \
  -DSHOW_DEBUG_INFO=OFF \
  -DDISPLAY_SHOW_TEMPERATURE=OFF \
  -DDISPLAY_SWAP_XY_IN_SOFTWARE=ON

echo -e "\e[32mCMake configuration completed.\e[0m"

sudo make -j
echo -e "\e[32mBuild completed successfully.\e[0m"