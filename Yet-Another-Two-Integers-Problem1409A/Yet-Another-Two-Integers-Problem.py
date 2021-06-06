from itertools import count

t = int(input())
for i in range(0, t):
    a, b = [int(x) for x in input().split()]
    # moves = [min(count(a + k or a - k)) for k in range(1, 10) if a + k == b or a - k == b]
    moves = abs(b - a) / 10
    if abs(b - a) % 10 != 0:
        moves += 1

    print(int(moves))
