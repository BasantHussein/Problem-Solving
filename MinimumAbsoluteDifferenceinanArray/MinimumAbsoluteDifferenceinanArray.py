import os


# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


def minimumAbsoluteDifference(arr):
    arr.sort()
    mini = abs(arr[0] - arr[1])
    for i in range(0, len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < mini:
            mini = abs(arr[i] - arr[i + 1])
    return mini


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
