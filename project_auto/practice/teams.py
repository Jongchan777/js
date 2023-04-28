import pyautogui
for i in range(5000):
    pyautogui.moveTo(500, 700, duration=3)
    pyautogui.moveTo(600, 800, duration=3)
    pyautogui.click(x=700, y=900, clicks=2, interval=3, button='left')
