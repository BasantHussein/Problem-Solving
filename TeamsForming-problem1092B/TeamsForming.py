n = int(input())
a = [int(x) for x in input().split()]
a.sort()
cntr = 0
i = 0
while i < len(a):
    cntr += abs(a[i] - a[i + 1])
    i += 2
print(cntr)
