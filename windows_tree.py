# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 23:35:55 2017

@author: windows_tree
this will run windows tree
"""

import pyautogui

# it's just open the run
pyautogui.keyDown('win')
pyautogui.press('r')
pyautogui.keyUp('win')

pyautogui.typewrite('tree')
pyautogui.press('enter')