from ctypes import c_size_t
from os import terminal_size
import time
from PIL.Image import NONE
import pyautogui
import pydirectinput

shortBreak = 0.1
midBreak = 0.25
longBreak = 0.5

def enterCommand(text):
    pydirectinput.press('t')
    time.sleep(shortBreak)
    pydirectinput.typewrite(text)
    time.sleep(shortBreak)
    pydirectinput.press('enter')
    time.sleep(shortBreak)
def stanBy():
    while(1):
        print('start')
        x = None
        x = pyautogui.locateOnScreen('lost_connection.PNG')
        if (x != None):
            pyautogui.click('lost_connection.PNG')
            time.sleep(longBreak)
            x = None
            x = pyautogui.locateOnScreen('server_logo.PNG')
            while (x == None):
                pyautogui.click('refresh_button.PNG')
                time.sleep(5)
                x = pyautogui.locateOnScreen('server_logo.PNG')
            pyautogui.doubleClick('server_logo.PNG')
            time.sleep(4)
            enterCommand('/login \%appdata\%')
            time.sleep(2)
            pydirectinput.rightClick()
            pydirectinput.click(750, 240)
            time.sleep(5)
            enterCommand('/is go')
        print('koniec')

def correctPosition():
    pydirectinput.move(0, -200)
    time.sleep(shortBreak)
    pydirectinput.move(200, 0)
    time.sleep(shortBreak)
    pydirectinput.move(-199, 199)
    time.sleep(shortBreak)
def chooseItem(item):
    if item == 'endRod':
        pydirectinput.press('1')
    if item == 'cobbleWall':
        pydirectinput.press('2')
    if item == 'fence':
        pydirectinput.press('3')
    if item == 'slab':
        pydirectinput.press('4')
    if item == 'sand':
        pydirectinput.press('5')
    if item == 'cactus':
        pydirectinput.press('6')
def placeItem(item, posX, posY):
    pydirectinput.move(posX, posY)
    chooseItem(item)
    pydirectinput.rightClick()
    time.sleep(shortBreak)
def placeCobbleWall(posX, posY):
    pydirectinput.move(posX, posY)
    chooseItem('cobbleWall')
    time.sleep(shortBreak)
    pydirectinput.keyDown('space')
    pydirectinput.keyUp('space')
    time.sleep(shortBreak)
    pydirectinput.rightClick()
    time.sleep(2 * shortBreak)
def placeCactus():
    placeItem('slab', 415, -290)
    placeItem('sand', -115, 20)
    placeItem('cactus', 0, 0)
    pydirectinput.move(-300, 270)
    time.sleep(shortBreak)
def throwOldItems():
    enterCommand('/enderchest')
    time.sleep(2*longBreak)
    pydirectinput.keyDown('shift')
    x = 540
    y = 510
    for i in range(0, 3):
        pydirectinput.click(x, y)
        time.sleep(longBreak)
        x += 36
    pydirectinput.keyUp('shift')
    pydirectinput.press('esc')
def getItems_column(num):
    enterCommand('/enderchest')
    if num == 1:
        x = 755
        for i in range(0, 3):
            y = 395
            for j in range(0, 4):
                pydirectinput.click(x, y)
                time.sleep(longBreak)
                pydirectinput.click(x-216, y)
                time.sleep(longBreak)
                y += 36
            x += 36
    if num == 2:
        x = 540
        y = 260
        for i in range(0, 3):
            for j in range(0, 4):
                pydirectinput.click(x+(j*36), y+(i*36))
                time.sleep(longBreak)
                pydirectinput.click(x+(i*36), y+140+(j*36))
                time.sleep(longBreak)
    if num == 3:
        x = 720
        y = 260
        for i in range(0, 3):
            for j in range(0, 4):
                pydirectinput.click(x+(j*36), y+(i*36))
                time.sleep(longBreak)
                pydirectinput.click(x-181+(i*36), y+140+(j*36))
                time.sleep(longBreak)
    x = 645
    y = 510
    for i in range(0, 3):
        pydirectinput.click(x+(i*36), y-(num*36))
        time.sleep(longBreak)
        pydirectinput.click(x+(i*36), y)
        time.sleep(longBreak)
    pydirectinput.press('esc')
    time.sleep(longBreak)
def getItems(num):
    enterCommand('/enderchest')
    time.sleep(longBreak)
    if num == 0:
        x = 750
        y = 390
        for i in range(0, 3):
            y = 390
            for j in range(0, 4):
                pydirectinput.click(x, y)
                time.sleep(longBreak)
                pydirectinput.click(x-210, y)
                time.sleep(longBreak)
                y += 36
            x += 36
    if num == 1:
        print("2")
    if num == 2:
        print("3")
    x = 645
    y = 465
    for i in range(0, 3):
        pydirectinput.click(x, y-(num*36))
        time.sleep(longBreak)
        pydirectinput.click(x, y+36)
        time.sleep(longBreak)
        x += 36
def fillItemBar(num):
    enterCommand('/enderchest')
    checkPart()
    time.sleep(longBreak)
    x = 540
    y = 0
    if num == 0:
        y = 390
    if num == 1:
        y = 426
    if num == 2:
        y = 462
    for i in range(0,3):
        pydirectinput.click(x, y)
        time.sleep(longBreak)
        pydirectinput.click(x, y+((3-num)*36))
        time.sleep(longBreak)
        x += 36
    checkNewItems()
    pydirectinput.press('esc')
    time.sleep(longBreak)
def buildColumn():
    for i in range(0, 4):
        correctPosition()
        for j in range(0, 16):
            placeCactus()
            for k in range(0, 2):
                placeItem('endRod', 0, -170)
                placeItem('endRod', 600, 0)
                placeCobbleWall(-600, 170)
            for k in range(0, 2):
                placeItem('fence', 0, -170)
                placeItem('fence', 600, 0)
                placeCobbleWall(-600, 170)
        if (i < 3):
            fillItemBar(i)
def checkPart():
    pydirectinput.move(0, -200)
    r = None
    r = pyautogui.locateOnScreen('finished_part.PNG')
    r = pyautogui.locateOnScreen('finished_part2.PNG')
    while (r == None):
        pydirectinput.press('esc')
        enterCommand('/sethome error')
        enterCommand('/is go')
        print("Error (part)")
        input("press enter to continue")
        time.sleep(5)
        r = pyautogui.locateOnScreen('finished_part.PNG')
        r = pyautogui.locateOnScreen('finished_part2.PNG')
    time.sleep(longBreak)
def checkNewItems():
    pydirectinput.move(0, -200)
    r = None
    r = pyautogui.locateOnScreen('new_items.PNG')
    while (r == None):
        pydirectinput.press('esc')
        enterCommand('/sethome error')
        enterCommand('/is go')
        print("Error (new items)")
        input("press enter to continue")
        time.sleep(5)
        r = pyautogui.locateOnScreen('new_items.PNG')
    time.sleep(longBreak)
def buildCactusFarm(quantity):
    if quantity >= 1:
        enterCommand('/home one')
        correctPosition()
        buildColumn()
    if quantity >= 2:
        enterCommand('/home two')
        getItems_column(1)
        correctPosition()
        buildColumn()
    if quantity >= 3:
        enterCommand('/home three')
        getItems_column(2)
        correctPosition()
        buildColumn()
    if quantity >= 4:
        enterCommand('/home four')
        getItems(3)
        correctPosition()
        buildColumn()
time.sleep(4)
buildCactusFarm(1)
enterCommand('/is go')





























