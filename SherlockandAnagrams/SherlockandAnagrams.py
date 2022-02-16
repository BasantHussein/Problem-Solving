
import os


#

# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    anags = 0
    dc = {}
    for i in range(len(s)):
        for j in range(len(s) - i):
            s1 = ''.join(sorted(s[j:j + i + 1]))
            if s1 in dc.keys():
                dc[s1] += 1
            else:
                dc[s1] = 1

    for k in dc.keys():
        anags += (dc[k] - 1) * dc[k] // 2
    return anags


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
