t = int(input())
perm_list = []

for i in range(0, t):
    p = int(input())
    perm_list = []
    for j in range(2, p + 1):
        perm_list.append(j)
    print(*perm_list, 1, sep=" ")
