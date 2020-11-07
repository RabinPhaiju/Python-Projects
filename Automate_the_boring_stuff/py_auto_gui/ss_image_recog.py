import pyautogui

# pyautogui.screenshot('ss.png') # take screenshot

# --------- top left corner -----------
# pos = pyautogui.locateOnScreen('7.png')
# print(pos)

# ----------- center -------------
pos = pyautogui.locateCenterOnScreen('7.png')
print(pos)
pyautogui.moveTo(1445, 626, 0.2)
pyautogui.click()