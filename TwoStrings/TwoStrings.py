# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2


def twoStrings(s1, s2):
    s3 = list("abcdefghijlkmnopqrstuvwxyz")
    flag = 0
    list_s1 = list(s1.strip())
    list_s2 = list(s2.strip())

    for e in s3:
        if e in list_s1 and e in list_s2:
            flag = 1
            break
    if flag == 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
