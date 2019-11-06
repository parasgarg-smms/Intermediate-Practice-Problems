#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    formed = ""
    for i in s:
        if i.isalpha():
            value = ord(i)+k
            if i.islower():
                while value>122:
                    diff = value - 122
                    value = 97 + diff-1
            if i.isupper():
                while value>90:
                    diff = value-90
                    value = 65+diff-1
            formed+=(chr(value))
        else:
            formed+=(i)
    print(formed)
    return formed


    pass

if __name__ == '__main__':
    fptr = open("output.txt", 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)
    print(result)

    fptr.write(result + '\n')

    fptr.close()
