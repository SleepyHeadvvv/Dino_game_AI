import pyautogui
import time
import keyboard
import win32api, win32con

time.sleep(0.5)
print("started")


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('q'):
    if pyautogui.pixel(550, 323)[0] == 83:
        keyboard.press('space')

    if pyautogui.pixel(481, 323)[0] == 83:
        keyboard.press('space') 
