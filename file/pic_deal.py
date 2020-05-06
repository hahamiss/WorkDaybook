from PIL import Image,ImageGrab,ImageColor
import time
import pyautogui

time.sleep(10)  #暂停

for ct in range(400):                  #截图张数
    im=ImageGrab.grab() #全屏截图
    width,heigh=im.size
    last=0;
    for i in range(width):
        colsum=0
        for j in range(heigh):
            (r,g,b)=im.getpixel((i,j))
            colsum=colsum+r+g+b
        if colsum-last>100 and last<100:
            colbegin=i
        if colsum-last<-100 and colsum<100:
            colend=i-1
        last=colsum
    im=im.crop((colbegin,0,colend,heigh-1))
    ls='./'+str(ct)+'.png'
    im.save(ls)
        
    pyautogui.press('enter')   #按下enter键
    time.sleep(1)
