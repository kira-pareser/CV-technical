import cv2
import numpy as np
import matplotlib.pyplot as plt


def correlation(img, kernel):
    h, w = img.shape
    h_kernel, w_kernel = kernel.shape

    # normalize image and kernel
    img = img / 255.0
    kernel = kernel / 255.0

    margin = w_kernel//2
    final = np.full((h, w), 255)

    for i in range(margin, h-margin):
        for j in range(margin, w-margin):
            result = img[i-margin:i + margin + 1, j-margin:j + margin + 1] * kernel
            final[i, j] = sum(sum(result))
            
    return final


if __name__=="__main__":
    # 1. Read images
    img = cv2.imread('9-ro.jpeg', 0)
    kernel = cv2.imread('template.png', 0)
    kernel = cv2.resize(kernel, (79,79))


    # 2. Tinh correlation
    final = correlation(img, kernel)


    # 3. Normalize anh sau khi tinh correlation
    max_vl, min_vl = int(max(map(max, final))), int(min(map(min, final)))
    final = final.astype("uint8")
    final = (final - min_vl) / (max_vl - min_vl) * 255

    # plt.imshow(final, cmap='gray')
    # plt.show()

    # 4. Count object in image
    final = final.astype("uint8")
    th, threshed = cv2.threshold(final, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    
    # findcontours
    cnts = cv2.findContours(threshed, cv2.RETR_LIST, 
                        cv2.CHAIN_APPROX_SIMPLE)[-2]
    

    # filter by area
    s1 = 3 # min square of object
    s2 = 40 # max square of object
    xcnts = []

    for cnt in cnts:
        if s1<cv2.contourArea(cnt) <s2:
            xcnts.append(cnt)

    print("Num objects: {}  ".format(len(xcnts)))