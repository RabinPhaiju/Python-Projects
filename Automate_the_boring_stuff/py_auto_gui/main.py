import pyautogui
import webbrowser
import time

# print(pyautogui.size()) # screen size
# print(pyautogui.position()) # mouse pos
# webbrowser.open('https://www.google.com') # open in default browser
# pyautogui.hotkey("ctrl", "t") # hotkey
# pyautogui.typewrite(["enter"]) # virtual type keyboard
# pyautogui.click(357, 64) # virtaul mouse click


# ----------- mouse move --------------
# pyautogui.move(300, 300)
# time.sleep(2)

# pyautogui.move(10, 10)
# pyautogui.move(10, 20, duration=2)
#
# pyautogui.moveRel(200, 200)
# pyautogui.moveRel(200, 200, duration=2)


pyautogui.click()
time.sleep(5)
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, 0.1) # move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, 0.1) # move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, 0.1) # move left
    distance = distance -25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, 0.1) # move  up

















