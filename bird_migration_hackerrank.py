#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    visit = []
    count_max=0
    returnvalue = 0
    for i in arr:
        if i not in visit:
            visit.append(i)
            count = arr.count(i)
            if count_max<count:
                count_max = count
                returnvalue = i
            elif count_max == count:
                if returnvalue>i:
                    returnvalue = i
    return returnvalue
    pass

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()