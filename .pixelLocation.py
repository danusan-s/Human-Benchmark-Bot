import keyboard
import pyautogui
import time

while True:
    if keyboard.is_pressed('g'):
        print(pyautogui.position())
        time.sleep(1)
