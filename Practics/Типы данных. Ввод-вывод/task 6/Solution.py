x = int(input())
a = x // 100
b = x // 10 % 10
c = x % 10

print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")