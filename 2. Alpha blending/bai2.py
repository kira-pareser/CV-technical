from statistics import correlation
import cv2
import numpy as np
import imageio

#load input
fg_raw = cv2.imread('mu.jpg')
mask_raw = cv2.imread('rmmu.png')
frames = imageio.mimread('rmfire.gif', '.gif')

fg_raw = cv2.cvtColor(fg_raw, cv2.COLOR_BGR2RGB)

#resize/editing image input
fg=cv2.resize(fg_raw, (600,350))
mask=cv2.resize(mask_raw, (600,350))
frames = [cv2.resize(frame,(1000,600)) for frame in frames]
for frame in frames:
    for i in range(0,4):
        cv2.imshow('asd',frame[:,:,i])
        cv2.waitKey(0)
    # frame[frame[:,:,1] != 0] = 255  
    # frame[frame[:,:,2] != 0] = 255  
    # frame[frame[:,:,0] != 0] = 255  
    
    #np.where((frame[:,:,1]!=0) & (frame[:,:,2]!=0)) = 255
imageio.mimsave('frames.gif', frames)

# resize effect gif to fit 
fg_h, fg_w, fg_c = fg.shape
bg_h, bg_w, bg_c = frames[0].shape
top = int((bg_h-fg_h)/2)
left = int((bg_w-fg_w)/2)

effect = [frame[top: top + fg_h, left:left + fg_w, 0:3] for frame in frames]


results = []
alpha = 0.6

# Test 1: effect inside mask

for i in range(len(effect)):
    result = fg.copy()
    result[mask != 0] = alpha * result[mask != 0]
    effect[i][mask == 0] = 0
    effect[i][mask != 0] = (1-alpha)*effect[i][mask != 0]
    result = result + effect[i]
    results.append(result)

imageio.mimsave('result.gif', results)






#Test 2: effect outside mask
# beta = []
# for j in range(fg_w):
#     beta.append(((fg_w/2 - j) / fg_w/2)**2)
   
# results2=[]

# for i in range(len(effect)):
#     result = fg.copy()
    

#     effect[i][mask != 0] = 0 #alpha * effect[i][mask != 0]

#     # effect[i][mask != 0] = 0
#     result[mask == 0] = alpha * result[mask == 0]
#     effect[i][mask == 0] = (1-alpha)*effect[i][mask == 0]


#     result = result + effect[i]
#     results2.append(result)
# imageio.mimsave('result2.gif', results2)




cv2.destroyAllWindows() 