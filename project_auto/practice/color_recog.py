from PIL import ImageGrab
import pyautogui
import os, tempfile, subprocess
import time

time.sleep(3)

# scr = ImageGrab.grab()
# scr.save('test_image.png')

scr = pyautogui.screenshot()

pos = pyautogui.position()
print(pos)

pix = scr.getpixel(pos)
print(pix)
