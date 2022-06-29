
import os

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a zero matrix table of size n+1*m+1
    dist_arr = [[0 for z in range(n + 1)] for z in range(m + 1)]

    # loop through the matrix
    for i, x in enumerate(s1):
        for j, y in enumerate(s2):
            if x == y:
                dist_arr[i + 1][j + 1] = dist_arr[i][j] + 1
            else:
                dist_arr[i + 1][j + 1] = \
                    max(dist_arr[i + 1][j], dist_arr[i][j + 1])
    return dist_arr[m][n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
