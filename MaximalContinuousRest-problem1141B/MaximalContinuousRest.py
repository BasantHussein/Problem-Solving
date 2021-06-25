n = int(input())
a = [str(x) for x in input().split()]
a2 = ''.join(a)
string = a2 * 2
l = []
cntr = 0
for i in range(0, len(string)):
    if string[i] == '1':
        cntr += 1
    elif string[i] == '0':
        l.append(cntr)
        cntr = 0
    else:
        l.append(cntr)

print(max(l))
