from collections import Counter

x = int(input())
s = [int(x) for x in input().split()]
sizes = Counter(s)
nc = int(input())
total = 0

for j in range(0, nc):
    cs, p = [int(b) for b in input().split()]
    if cs in sizes.keys() and cs in s:
        total += p
        s.remove(cs)
        sizes.update(s)

print(total)
