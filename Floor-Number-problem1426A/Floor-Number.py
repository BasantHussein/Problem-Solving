t = int(input())
for i in range(0, t):
    n, x = [int(j) for j in input().split()]
    cntr = 0
    n -= 2
    cntr += 1
    while n > 0:
        n -= x
        cntr += 1
    print(cntr)
