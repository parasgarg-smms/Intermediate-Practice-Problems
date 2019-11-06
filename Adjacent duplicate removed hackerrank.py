#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superReducedString function below.
def superReducedString(s):
    dup = list(s)
    j=0
    for _ in range(len(s)):
        flag = 0
        for i in range(len(dup) - 1):
            arr = dup[i:i + 2]
            if arr[0] == arr[1]:
                flag = 1
                d = dup.pop(i)
                d = dup.pop(i)
                break
        if flag == 0:
            break

    if s == "":
        return "Empty String"
    else:
        return "".join(dup)


if __name__ == '__main__':
    fptr = open("output.txt", 'w')

    s = input()

    result = superReducedString(s)
    print(result)
    fptr.write(result + '\n')

    fptr.close()
