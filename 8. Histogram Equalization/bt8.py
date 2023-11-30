import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img.jpeg", 0)
#Tính toán histogram
def compute_hist(img):
    hist = np.zeros((256,), np.uint8)
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i][j]] += 1
    return hist

#Cân bằng histogram 
def equal_hist(hist):
    cumulator = np.zeros_like(hist, np.float64)
    for i in range(len(cumulator)):
        cumulator[i] = hist[:i].sum()
    print(cumulator)
    new_hist = (cumulator - cumulator.min())/(cumulator.max() - cumulator.min()) * 255
    new_hist = np.uint8(new_hist)
    return new_hist



def plot_img_and_hist(img):
  '''Draw image together with its histogram and cdf'''
  hist = cv2.calcHist(
              [img],
              channels=[0],
              mask=None, #full image
              histSize=[256], #full scale
              ranges=[0,256]
  )
  h,w = img.shape[:2]
  normalized_hist = hist/(h*w)
  cdf = normalized_hist.cumsum()
  plt.subplot(1,2,1)
  plt.imshow(img, cmap = 'gray')
  plt.subplot(1,2,2)
  plt.plot(normalized_hist, 'r')
  plt.plot(cdf, 'b--')
  plt.legend(('histogram', 'cdf'), loc = 'upper left')

hist = compute_hist(img).ravel()

new_hist = equal_hist(hist)

h, w = img.shape[:2]
for i in range(h):
   for j in range(w):
       img[i,j] = new_hist[img[i,j]]
       
fig = plt.figure()
ax = plt.subplot(121)
plt.imshow(img, cmap='gray')
plot_img_and_hist(img)

# plt.subplot(122)
# plt.plot(new_hist)
plt.show()