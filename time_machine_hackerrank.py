#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if (year % 4 == 0 and year % 100 != 0) or (year%400==0):
        return("12.09.{}".format(year))
    else:
        return("13.09.{}".format(year))
if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)
    fptr.write(result + '\n')

    fptr.close()