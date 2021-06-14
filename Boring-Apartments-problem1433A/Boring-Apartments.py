t = int(input())

for i in range(0, t):
    x = int(input())
    digit = x % 10
    cnt = 0
    while int(x) > 0:
        x = x / 10
        cnt += 1

    if cnt == 1:
        print(((digit * 10) - 10) + 1)
    elif cnt == 2:
        print(((digit * 10) - 10) + 3)
    elif cnt == 3:
        print(((digit * 10) - 10) + 6)
    elif cnt == 4:
        print(((digit * 10) - 10) + 10)

