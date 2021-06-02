from math import floor

t = int(input())
for i in range(0, t):
    n = int(input())

    if n % 2 != 0:
        total = floor(n / 2)
    if n % 2 == 0:
        total = floor((n / 2) - 1)
    if floor(n / 2) == 0 or n / 2 == 1:
        total = 0
    #if n / 2 == n - (n / 2):
        #total = 0
    print(total)
