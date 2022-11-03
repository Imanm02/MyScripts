from inspect import Parameter
from time import sleep
import pyautogui as user

sleep(5)
user.moveTo(80, 529)
for i in range(400):
    img = user.screenshot()
    img.save(f"book/{i}.jpg")
    user.click()
    sleep(0.5)

