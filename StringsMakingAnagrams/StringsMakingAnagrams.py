#!/bin/python3

import os

from collections import Counter


# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    a_count_dict = Counter(a)
    b_count_dict = Counter(b)
    count = 0
    for k in a_count_dict.keys():
        if k in b_count_dict.keys():
            count += abs(a_count_dict[k] - b_count_dict[k])
        else:
            count += a_count_dict[k]

    for k in b_count_dict.keys():
        if k not in a_count_dict.keys():
            count += b_count_dict[k]
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
