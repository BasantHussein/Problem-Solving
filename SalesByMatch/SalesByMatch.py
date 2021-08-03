#!/bin/python3

import math
import os
from collections import Counter


#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    c = 0
    count_pairs = Counter(ar)
    for key in count_pairs:
        if count_pairs[key] % 2 == 0:
            c += count_pairs[key] / 2
        elif count_pairs[key] % 2 != 0 and count_pairs[key] != 1:
            c += math.floor(count_pairs[key] / 2)
    return int(c)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
