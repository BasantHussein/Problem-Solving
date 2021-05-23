x1, x2, x3, x4 = [int(x) for x in input().split()]
x = max(x1, x2, x3, x4)
if x - x1 > 0:
    a = x - x1
    print(a)

if x - x2 > 0:
    b = x - x2
    print(b)

if x - x3 > 0:
    c = x - x3
    print(c)

if x - x4 > 0:
    d = x - x4
    print(d)
