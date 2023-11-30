import matplotlib.pyplot as plt
import numpy as np


def generate_data(n,ratio):
    nrounded = round(n*ratio)
    m = np.random.randint(1,10)
    c = np.random.randint(2,6)

    xd = np.linspace(0, n, num=nrounded,dtype=int, endpoint=True)
    yd = np.array([m*i + c  for i in xd])

    x=np.concatenate((xd,np.random.randint(0,n,size=n-nrounded)),axis=None)
    y=np.concatenate((yd,np.random.randint(0,n,size=n-nrounded)),axis=None)

    points =  np.concatenate((x.reshape(-1,1),y.reshape(-1,1)),axis=1)   
    return points

def fx(x, y, ab):
    xa, ya, xb, yb = ab[0, 0], ab[0, 1], ab[1, 0], ab[1, 1]
    k = 
    c = 
    return 1 if abs() < 0.001 else 0


n = 10; ratio=0.7
dataset = generate_data(n,ratio)
# index = np.random.choice(n, 2, replace=False)  
# ab = dataset[index]   #doan AB
# print(ab)

while True: 
    index = np.random.choice(n, 2, replace=False)  
    ab = dataset[index]

    count = 0
    for i in dataset: 
        count += fx(i[0], i[1], ab)

    if count >= round(n*ratio): 
        xa, ya, xb, yb = ab[0, 0], ab[0, 1], ab[1, 0], ab[1, 1]
        print('PTDT: d = %.2f * (x - %.2f) + %.2f * (y - %.2f) = 0'%((ya - yb), xa, (xb - xa), yb))
        plt.scatter(dataset[:, 0], dataset[:, 1])
        plt.xlim(-5, np.amax(dataset)+10), plt.ylim(-5, np.amax(dataset)+10)
        plt.plot((xa, ya), (xb, yb), 'r',marker='o')
        plt.show()
        break


