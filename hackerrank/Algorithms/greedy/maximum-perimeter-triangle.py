#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    n = len(sticks)
    arr = sorted(sticks, reverse=True)
    i = n-1
    for i in range(n-2):
        if arr[i] < arr[i+1] + arr[i+2]:
            return [arr[i+2], arr[i+1], arr[i]]
    return [-1]


if __name__ == '__main__':
    sticks = [9, 2015, 5294, 58768, 285, 477, 72, 13867, 97, 22445, 48, 36318, 764, 8573, 183, 3270, 81, 1251, 59, 95094]
    ret = maximumPerimeterTriangle(sticks)
    print(ret)
