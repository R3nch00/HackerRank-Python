#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
 
def time_delta(t1, t2):
    format_str = '%a %d %b %Y %H:%M:%S %z'
    time1 = datetime.strptime(t1, format_str)
    time2 = datetime.strptime(t2, format_str)
    
    # Calculate the absolute difference in seconds
    delta_seconds = abs(int((time1 - time2).total_seconds()))
    
    return str(delta_seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input("Enter the number of testcases: "))

    for t_itr in range(t):
        t1 = input("Enter timestamp 1: ")
        t2 = input("Enter timestamp 2: ")

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()