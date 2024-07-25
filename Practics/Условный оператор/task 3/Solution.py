x = int(input())
a = x // 1000
b = x // 100 % 10
c = x // 10 % 10
d = x % 10
sum = a + d
raz = b - c
if sum == raz:
    print('ДА')
else:
    print('НЕТ')