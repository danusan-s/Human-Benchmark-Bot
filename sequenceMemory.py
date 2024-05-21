import pyautogui
import time

# Works till 8

posn = [(1080,500),(1280,500),(1480,500),(1080,700),(1280,700),(1480,700),(1080,900),(1280,900),(1480,900)]
sequence=[]

time.sleep(2)
pyautogui.click(1280,850)
time.sleep(1)

delay=0.5

while True:
    sim = pyautogui.screenshot(region=(980,400,600,600))
    '''if (len(sequence)==8):
        sim = sim.save('test.jpg')
        print[sequence]
        break'''
    for i in range(9):
        if (sequence and sequence[-1]==i):
            continue
        if (sim.getpixel((posn[i][0]-980,posn[i][1]-400))==(255,255,255)):
            sequence.append(i)
            time.sleep(1)
            break
    for j in sequence:
        pyautogui.click(posn[j][0],posn[j][1])
    sim = sim.save(f"test_{len(sequence)}.jpg")
    delay+=0.005
    time.sleep(1 + len(sequence)*delay)

#1 sec after complete