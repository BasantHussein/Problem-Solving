str = input()
c = 0
x = len(str)
for i in range(0, x):
    j = i + 1
    for j in range(j, x):
        k = j + 1
        for k in range(k, x):
            if str[i] == 'Q' and str[j] == 'A' and str[k] == 'Q':
                c = c + 1

print(c)
