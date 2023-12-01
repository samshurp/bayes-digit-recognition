import numpy as np
from matplotlib import pyplot as plt

matrix = 28 
with open('data2', 'rb') as fid: 

    # t1 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
    # t2 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
    # t3 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
# plt.subplot(131)
# plt.imshow(t1)
# plt.show()

    # for _ in range (4): 
    for _ in range(1): 
        img = np.fromfile(fid, dtype=np.uint8, count=matrix*matrix).reshape((matrix,matrix))
        plt.imshow(img)
        plt.show()
        print(img)


*************************************
*** Nov 28, 2023 ***

    import numpy as np
from matplotlib import pyplot as plt

matrix = 28 
with open('/Users/sam_sherpa/Desktop/Python txt/digitdata/data2', 'rb') as fid: 

    # t1 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
    # t2 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
    # t3 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
# plt.subplot(131)
# plt.imshow(t1)
# plt.show() 

    # for _ in range (4): 
    for _ in range(1): 
        img = np.fromfile(fid, dtype=np.uint8, count=matrix*matrix).reshape((matrix,matrix))
        # plt.imshow(img)
        # plt.show()
        print(img)
        V1 = img.flatten()
        print(V1)
        TotalV1 = np.sum(V1)
        print(TotalV1)
        Pprob = V1 / TotalV1
        print(Pprob) 

********************************* 
******** Latest - Nov 30 ******

import numpy as np
from matplotlib import pyplot as plt

# For number 0 
data_mean = []
data_std = []

matrix = 28
threshold = 128
base_path = '/Users/sam_sherpa/Desktop/Python txt/digitdata/'
Sum_vector = np.zeros((matrix * matrix,))
V = {}

with open('/Users/sam_sherpa/Desktop/Python txt/digitdata/data0', 'rb') as fid: 
    for i in range(1000):
        img = np.fromfile(fid, dtype=np.uint8, count=matrix*matrix).reshape((matrix, matrix))
        # plt.imshow(img)
        # plt.show()
        binary_image = np.where(img >= threshold, 1, 0)
        V[i] = binary_image.flatten()

    matrix = np.vstack([V[i] for i in range(1000)]) 
    # Calculate mean and standard deviation for each column
    meanColumn = np.mean(matrix, axis=0)
    stdColumn = np.std(matrix, axis=0)
    Print('')
    print(meanColumn)
    print('Next- Standard Deviation')
    print(stdColumn)





