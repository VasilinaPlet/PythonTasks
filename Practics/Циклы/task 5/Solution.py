m = 1000
while True:
    x = int(input())
    if x == 0:
        break
    if -999 <= x <= -100 or 100 <= x <= 999:
        if x < m:
            m = x
if m < 1000:
    print(m)
else:
    print('NO')