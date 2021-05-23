t = int(input())

for i in range(0, t):
    inputs = []
    a, b, c, n = [int(x) for x in input().split()]
    inputs = [a, b, c]
    sum = a + b + c + n
    if sum % 3 == 0 and a <= sum / 3 and b <= sum / 3 and c <= sum / 3:
        print("YES")
    else:
        print("NO")
