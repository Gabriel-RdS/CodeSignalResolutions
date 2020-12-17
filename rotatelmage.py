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

# or


def rotateImage3(a):
    return [[x[i] for x in a][::-1] for i in range(len(a))]
