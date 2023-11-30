import numpy as np
import random
import matplotlib.pyplot as plt

# fx = 3x + 2 -> 3x -2y = 0
x = np.array(tuple([random.randrange(20) for i in range(50)]))[:10]
y = np.concatenate((3 * x[:7] + 2, [23, 5, 2]), axis=0)
data = np.concatenate((x.reshape(-1, 1), y.reshape(-1, 1)), axis=1)
print(data.shape)

# viet phuong trinh duong thang
def fx(x, y, sub_arr):
    a, b, c, d = sub_arr[0, 0], sub_arr[0, 1], sub_arr[1, 0], sub_arr[1, 1]
    return 1 if (b-d) * (x - a) + (c - a) * (y - b) == 0 else 0


ratio = 0.7
while True: 
    # 1. random 2 diem
    n = 2  # for 2 random indices
    index = np.random.choice(x.shape[0], n, replace=False)  
    sub_arr = data[index]

    # check cac diem con lai
    count = 0
    for i in data: 
        count += fx(i[0], i[1], sub_arr)


    if count / data.shape[0] >= ratio: 
        a, b, c, d = sub_arr[0, 0], sub_arr[0, 1], sub_arr[1, 0], sub_arr[1, 1]
        print('Phuong trinh duong thang la: %.2f * (x - %.2f) + %.2f * (y - %.2f) = 0'%((b - d), a, (c - a), b))
        # # ve
        # plt.scatter(data[:, 0], data[:, 1])
        # plt.xlim(0, 50), plt.ylim(0, 70)
        # plt.plot((a, b), (c, d), marker = 'o')
        # plt.show()
        break