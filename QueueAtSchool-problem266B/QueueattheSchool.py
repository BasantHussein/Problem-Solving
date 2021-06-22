n, t = [int(x) for x in input().split()]
s = input()
s = list(s)
j = 0
for i in range(0, t):
    j = 0
    while j < (len(s) - 1):
        if s[j] == 'B' and s[j + 1] == 'G':
            s[j] = 'G'
            s[j + 1] = 'B'
            j += 2
        else:
            j += 1

print(''.join(s))

