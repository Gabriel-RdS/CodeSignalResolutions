"""
Link of challange: https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB/description
"""

import numpy as np


def rotateImage(array):
    return np.rot90(array, k=3, axes=(0, 1))

