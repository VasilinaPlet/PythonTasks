a = int(input())
b = int(input())
c = int(input())
d = int(input())
r = 0
z = 0
if a < b:
    r = a
else:
    r = b
if c < d:
    z = c
else:
    z = d
if r < z:
    print(r)
else:
    print(z)