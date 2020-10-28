
# Imports
from time import sleep
import keyboard
import pyautogui

# Constants
filename = "file.txt"

sleep(4)
print('start')
with open(filename) as file_object:
        for line in file_object:
            if line != ' ':
                pyautogui.typewrite(line)
                sleep(0.1)
                pyautogui.press("enter")
                sleep(0.1)
		
