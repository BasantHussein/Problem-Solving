s = input()
t = input()

hour = int(s[:2]) - int(t[:2])
minutes = int(s[3:5]) - int(t[3:5])
if minutes < 0:
    minutes+=60
    hour-=1

if hour < 0:
    hour+=24

print("{:02}:{:02}".format(hour, minutes))