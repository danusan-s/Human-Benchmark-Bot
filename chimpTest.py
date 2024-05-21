import pytesseract
import pyautogui
from PIL import ImageGrab, Image, ImageDraw
import time

# x grid gap = 130, y grid gap = 130
# x max = 1755 , y max = 915, x min = 805, y min = 375
# 5*8 grid ?

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

level = 5
posn = {}
time.sleep(2)
pyautogui.click(1280,880)
time.sleep(1)

while True:
    for i in range(805,1755,135):
        for j in range(375,916,135):
            img = ImageGrab.grab(bbox=(i-45,j-45,i+45,j+45))
            image = Image.new('RGB', (1000, 1000), color=(43,135,209))
            draw = ImageDraw.Draw(image)
            image.paste(img,(500,500))
            number = pytesseract.image_to_string(image,config='--psm 6 -c tessedit_char_whitelist=0123456789')
            if number:
                print(number)
                posn[int(number)] = (i,j)
    for k in range(1,level):
        pyautogui.click(posn[k][0],posn[k][1])
    level+=1
    time.sleep(0.5)
    pyautogui.click(1280,855)
    time.sleep(0.5)
