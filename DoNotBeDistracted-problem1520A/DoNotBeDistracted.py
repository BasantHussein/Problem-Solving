t = int(input())
for i in range(0, t):
    n = int(input())
    s = input()
    checked_list = []
    for j in range(len(s) - 1):
        if n == 1:
            checked_list.append(s[0])
        elif s[j] == s[j + 1] and s[j] not in checked_list:
            checked_list.append(s[j])
        elif s[j] != s[j + 1]:
            if s[j] not in checked_list:
                checked_list.extend([s[j], s[j + 1]])
            elif s[j] in checked_list:
                checked_list.extend(s[j + 1])

    if len(set(checked_list)) == len(checked_list):
        print("YES")
    else:
        print("NO")


