"""
Link of challange: https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB/description
"""

import numpy as np


def rotateImage(array):
    return np.rot90(array, k=3, axes=(0, 1))

# or


def rotateImage2(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a


# Testes
array1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(rotateImage(array1))
print(rotateImage2(array1))

