#!/bin/python3

import math
import os
import random
import re
import sys

def substrings(n):
    MOD = 1000000007
    length = len(n)
    
    sum_of_digit = [] 
    sum_of_digit.append(int(n[0]))
    result = sum_of_digit[0]
    
    for i in range(1, length):
        number_i = int(n[i])
        sum_of_digit.append((10 * sum_of_digit[i - 1] + (i + 1)*number_i )%MOD)
        result += sum_of_digit[i]%MOD
    #print(sum_of_digit)
    return result%MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
