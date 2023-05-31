#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pyautogui
import time
import pyperclip
pyautogui.hotkey("win","d")
time.sleep(1)
pyautogui.doubleClick(1502,1006)
X,Y=pyautogui.locateCenterOnScreen(r"C:\Users\mkuno5808\Desktop\MS\icon.png")
pyautogui.doubleClick(X,Y)
time.sleep(2)
pyautogui.click(187,393)
pyperclip.copy("テスト")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl","s")
pyautogui.click(1896,30)
print("処理は終了しました。")


# In[ ]:





# In[ ]:




