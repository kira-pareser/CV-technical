 from locale import normalize
import numpy as np
import cv2 
from scipy import signal
import matplotlib.pyplot as plt

def corr(H, F):
    h, w = F.shape
    G = np.zeros((H.shape[0] - h + 1, H.shape[1] - w + 1))
    for i in range(G.shape[0]):
        for j in range(G.shape[1]):
            G[i, j] = (H[i: i + h, j: j + w] * F).sum()
    return G
    
def conv(H, F):
    F2 = np.flip(F)
    return corr(H,F2)


img = cv2.imread("9ro.jpeg", 0)
img2 = cv2.imread('ro.png')

F = np.full((3,3),1/9)
K = np.array([[1, 0, 0],[0, 1, 1],[1, 0, 1]])

# result1 = corr(img,K)
result1 = corr(img,F)
# norm = np.zeros(result1.shape)
# normalize_result = cv2.normalize(result1,  norm, 0, 255, cv2.NORM_MINMAX)

plt.imshow(result1)
plt.show()

# cv2.imshow("a",normalize_result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()