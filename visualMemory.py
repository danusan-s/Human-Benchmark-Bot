import pyautogui
from PIL import ImageGrab
import time

time.sleep(2)
pyautogui.click(1280,820)
time.sleep(0.5)

def clickWhites(img):
    first = True
    for i in range (0,img.width,50):
        for j in range(0,img.height,50):                #in the future change it so increment changes by level, so it doesnt give out eventually
            if img.getpixel((i,j))==(255,255,255):
                if first:
                    time.sleep(1)
                    first=False
                pyautogui.click(915+i,365+j)
            if pyautogui.pixel(700,600)!=(43, 135, 209):
                return

while True:
    time.sleep(0.34) # magic number, it works (also 34 is funny)
    img = ImageGrab.grab(bbox=(915,365,1680,1037))
    clickWhites(img)

# Score of 38 acheived