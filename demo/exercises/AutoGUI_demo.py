# pyAutoGUI小例子
# http://www.51testing.com/html/41/n-4479141.html

import pyautogui
distance = 100

pyautogui.moveTo(400, 300)
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.1)
    distance -= 5
    pyautogui.drag(0, distance, duration=0.1)
    pyautogui.drag(-distance, 0, duration=0.1)
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.1)