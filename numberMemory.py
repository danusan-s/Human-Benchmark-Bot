import pyautogui
import time
import pytesseract
from PIL import ImageGrab, Image, ImageDraw

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(2)
pyautogui.click(1280,890)
time.sleep(0.5)
level=1


while True:
    img = ImageGrab.grab(bbox=(600,300,2000,700))
    image = Image.new('RGB', (1500,1000), color=(43,135,209))
    draw = ImageDraw.Draw(image)
    img = img.resize((350,100))
    image.paste(img,(0,0))  # pasted screenshot onto larger canvas so number recognition is better
    number = pytesseract.image_to_string(image,config='--psm 6 -c tessedit_char_whitelist=0123456789')
    # print(number) to see number recognized
    # image = image.save(f"test_{level}.jpg") to save image
    time.sleep(level+1)
    level+=1
    pyautogui.typewrite(number)
    time.sleep(1)
    pyautogui.click(1280,790)
    time.sleep(0.3)
    pyautogui.click(1280,880)
    time.sleep(0.1)
