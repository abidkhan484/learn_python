# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:30:54 2017

@author: abid
"""
# this program auto refresh my computer

import pyautogui
import time

time.sleep(1)

pyautogui.click(x=1364, y=766)

click = 20
while click:
    pyautogui.click(x=494, y=230, interval=0.2, button='right')
    pyautogui.click(x=553, y=286)
    
    click -= 1