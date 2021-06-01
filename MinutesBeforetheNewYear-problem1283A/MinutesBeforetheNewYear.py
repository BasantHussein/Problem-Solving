t = int(input())
for i in range(0, t):
    h, m = [int(x) for x in input().split()]
    hours = 0 - h
    minutes = 0 - m
    if minutes < 0:
        minutes += 60
        hours -= 1
    if hours < 0:
        hours += 24
    total_minutes = hours * 60 + minutes
    print(total_minutes)
