import pyautogui as gui




while True:
     last_position=gui.position()
     if last_position!=gui.position():
         print(gui.position())