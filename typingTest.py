import pyautogui
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(2)

img = pyautogui.screenshot(region=(510,566,2153,887))
text = pytesseract.image_to_string(img)
text = text.split()

if text[0][0]=='|':
    temp = text[0][1:]
    text[0]=temp

def parse(text):
    parsed = ""
    for word in text:
        if word=="aN":
            return parsed
        for char in word:
            if char==':':
                return parsed
        if word=='|':
            parsed += "I "
        else:
            parsed+=word + ' '
final = parse(text)
print(final)
pyautogui.typewrite(final)

