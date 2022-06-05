import os

import collections


#

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    s = list(s)
    freq_dict = dict(collections.Counter(s))
    if len(set(freq_dict.values())) <= 1:
        return "YES"

    else:

        count_dict = dict(collections.Counter(freq_dict.values()))

        maxi = max(count_dict.values())
        inverted_count_dict = dict(map(reversed, count_dict.items()))
        maxi = inverted_count_dict[maxi]

        for k in freq_dict.keys():
            if freq_dict[k] != maxi:
                check = freq_dict[k] - 1
                if check == maxi:
                    freq_dict[k] = check
                    if len(set(freq_dict.values())) <= 1:
                        return "YES"
                    else:
                        return "NO"
                elif check == 0 and count_dict[freq_dict[k]] == 1:

                    if len(set(freq_dict.values())) - 1 <= 1:
                        return "YES"
                    else:
                        return "NO"


                else:
                    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
