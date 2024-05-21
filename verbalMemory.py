import pyautogui 
import pytesseract
from PIL import ImageGrab
import time

seen =set()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(2)
pyautogui.click(1280,890)
time.sleep(1)

while True:
    word = ImageGrab.grab(bbox=(766,590,1753,692))
    recognized_text = pytesseract.image_to_string(word)
    if (recognized_text in seen):
        pyautogui.click(1180,770)
    else:
        pyautogui.click(1385,770)
        seen.add(recognized_text)

# went up to 200 without losing a life, ended manually , could be pushed way further