import os


# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. n the number of contests
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY contests


def luckBalance(n, k, contests):
    luck_sum = 0
    contests.sort(reverse=True)
    for j in range(n):
        if contests[j][1] == 0:
            luck_sum += contests[j][0]
        elif k > 0:
            k -= 1
            luck_sum += contests[j][0]
        else:
            luck_sum -= contests[j][0]
    return luck_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(n, k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
