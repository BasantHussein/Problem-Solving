s = input()
if len(s) == 1:
    print(s)
else:
    x = s.replace("+", " ")
    res = ''.join(sorted(x))
    w = res.replace("", "+")[len(res):-1]
    print(w)
