import numpy as np
import cv2
import matplotlib.pyplot as plt

#đọc điểm chroma và tính hsv
ch_key = cv2.imread("ch_key.jpg",1)
ch_point = np.uint8([[ch_key[1,1,:]]])
cvt_point = cv2.cvtColor(ch_point, cv2.COLOR_BGR2RGB)

#đặt threshold 
min = np.array(cvt_point[0,0,:])
max = np.array(cvt_point[0,0,:])
min[0]=0; max[0]=100 #red
min[1]=100 #green
min[2]=0; max[2]=100 #blue

#đọc ảnh và tính HSV
img = cv2.imread("img.jpg",1)
cvt_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

mask = cv2.inRange(cvt_img, min, max)
mask = 255 - mask
final = cv2.bitwise_and(img, img, mask=mask)

effect = cv2.imread("effect.jpg",1)
effect = cv2.resize(effect, (img.shape[1], img.shape[0]))


result = effect.copy()
result[mask != 0] = final[mask != 0]
cv2.imwrite('result.png',result)

