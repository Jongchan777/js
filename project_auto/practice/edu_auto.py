import pyautogui, time


time.sleep(5)

#print(pyautogui.position()) # current mouse x and y

#Point(x=1080, y=841)(['2배'])
#Point(x=1253, y=844)(['>'])
#Point(x=1058, y=170)(Alert 종료)

for i in range(100):
    pyautogui.click(x=1080, y=841, clicks=1, interval=2, button='left') 
    time.sleep(2)
    pyautogui.click(x=1253, y=844, clicks=1, interval=2, button='left') 
    time.sleep(2)
    pyautogui.click(x=1058, y=170, clicks=1, interval=2, button='left') 
    time.sleep(2)
    print(i)