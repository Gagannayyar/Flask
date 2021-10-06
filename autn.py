import pyautogui as pag
import time

n = 0

while n < 1000:
    pag.moveRel(100, 0, duration=5)
    pag.click()
    time.sleep(3)
    pag.moveRel(0, 100, duration=5)
    pag.click()
    time.sleep(3)
    pag.moveRel(-100, 0, duration=5)
    pag.click()
    time.sleep(3)
    pag.moveRel(0, -100, duration=5)
    pag.click()
    time.sleep(3)
    n += 1
