"""
import os


cp = os.getcwd()

print(cp)
"""

"""
import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break
"""

import keyboard, pyautogui

while True:
    while True: 
        if keyboard.is_pressed('q'):
            pos = pyautogui.position()
            print(pos)
            break
    while True:
        if keyboard.is_pressed('o'):
            break
        #opoqqqqqoqoqoqoqoqoqoqoqoqoqoqoqoqoqoqoq