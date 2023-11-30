import cv2
import numpy as np

#load input
img1=cv2.imread('girl.jpg')
img2 = img1 #dùng hình 1 cho tiện
h,w,c = img1.shape #trích xuất kích thước ảnh

for i in range(w-1,0,-50): #đi từ phải qua trái
    #chia thanh 2 phan
    edit1 = img1[:,:i]  #bỏ đi 1 phần của hình 1  
    edit2 = img2[:,:w-i] #lấy 1 phần của hình 2
    img = np.concatenate((edit1,edit2),axis=1) #ghép phần của hình 2 trám vào phần bỏ đi của hình 1
    cv2.imshow('img',img)
    cv2.waitKey(1)