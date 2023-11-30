import cv2
import numpy as np

img=cv2.imread("a.png",0)
img=-img
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 7)
dilation = cv2.dilate(erosion,kernel,iterations = 2)
thresh = cv2.threshold(dilation, 5, 255, cv2.THRESH_BINARY)[1]

numLabels, labels, = cv2.connectedComponents(thresh, 4, cv2.CV_32S)
print("So label dem duoc: ", numLabels)
cv2.imshow("Input", thresh)
cv2.waitKey(0)
