import pyautogui
import time

# Define the coordinates of the pixel you want to monitor
pixel_x = 50
pixel_y = 652
count=0

while True:
    # Capture the color of the specified pixel
    pixel_color = pyautogui.pixel(pixel_x, pixel_y)
    if (pixel_color==(75, 219, 106)):
        pyautogui.click(pixel_x,pixel_y)
        time.sleep(1)
        pyautogui.click(pixel_x,pixel_y)
        count+=1
    if count==5:
        break
    