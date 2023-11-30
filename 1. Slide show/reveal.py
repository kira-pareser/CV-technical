import cv2
import numpy as np
from math import ceil
import os

img2=cv2.imread('logo.jpg')
img1=cv2.imread('girl.jpg')
img =[img1,img2]
result = np.zeros((360,360,3), np.uint8)
i=0
a = 1.0
b = 0.0
cur = img1
while(True):

    if(ceil(a)==0):
        a = 1.0
        b = 0.0
        cur = img[i+1]
        cur = cv2.resize(cur, (360, 360))

    a -= 0.01
    b += 0.01

    result = cv2.addWeighted(result, a, cur, b, 0)
    cv2.imshow("Slide Show", result)
    key = cv2.waitKey(1) & 0xff
    if key==ord('q'):
        break

cv2.destroyAllWindows()