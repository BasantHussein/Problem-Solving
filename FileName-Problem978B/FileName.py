n = int(input())
s = input()
s = list(s)
cntr = 0
cntr2 = 0
for i in range(0, len(s)):
    if s[i] == 'x':
        cntr += 1
    elif s[i] != 'x':
        cntr = 0
    if cntr >= 3:
        cntr2 += 1
print(cntr2)
