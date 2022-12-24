import os
import pyautogui
import time
from python_imagesearch.imagesearch import imagesearch

#os.system('C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\MPTool')
print('py tool test : open MPtool....')
os.popen('..\MPTool\SM2504_MPTool.exe')
time.sleep(5)
pos = imagesearch("parameter.png")
print(pos)
pyautogui.moveTo(pos[0]+30,pos[1]+10)
time.sleep(1)
pyautogui.click()

time.sleep(1)
pos = imagesearch("bin.png")
print(pos)
pyautogui.moveTo(pos[0]+40,pos[1]+50)
time.sleep(1)
pyautogui.click()

#print('Bin file xfer to FTP...')



    