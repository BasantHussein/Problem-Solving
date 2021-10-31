from collections import Counter


# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    magazine_dict = Counter(magazine.split())
    note_dict = Counter(note.split())
    count = 0
    flag = 0
    lk = len(note_dict.keys())
    for k, v in note_dict.items():
        if k in magazine_dict.keys():
            if note_dict[k] <= magazine_dict[k]:
                count += 1
        else:
            flag = 1
            break
    if count == lk and flag == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input()
    note = input()

    checkMagazine(magazine, note)
