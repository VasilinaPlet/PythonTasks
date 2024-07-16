x = int(input())
tis = x // 1000 % 10
sot = x // 100 % 10
des = x // 10 % 10
ed = x % 10
print(tis * sot * des * ed)