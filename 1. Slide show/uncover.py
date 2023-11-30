import cv2
import numpy as np

#load input
img1=cv2.imread('girl.jpg')
img2 = img1
h,w,c = img1.shape #trich xuat kich thuoc anh

#ương tự cover
for i in range(0,w,50): #đi từ phải qua trái??

    edit1 = img1[:,i:] #vì 
    edit2 = img2[:,w-i:]
    img = np.concatenate((edit1    ,edit2),axis=1)
    cv2.imshow('img',img)
    
    cv2.waitKey(1)