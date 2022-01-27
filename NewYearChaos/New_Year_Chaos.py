#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    one = 1
    two = 2
    third = 3
    count = 0
    for i in range(len(q)):
        if q[i] == one:
            one = two
            two = third
            third += 1
        elif q[i] == two:
            count += 1
            two = third
            third += 1
        elif q[i] == third:
            count += 2
            third += 1
        else:
            return "Too chaotic"
    return count


q = list(map(int, input().rstrip().split()))
print(minimumBribes(q))
