x = int(input())
seconds = x % 60
x //= 60
minutes = x % 60
x //= 60
hours = x % 24
print(hours // 10, hours % 10, ":", minutes // 10, minutes % 10, ":", seconds // 10, seconds % 10, sep="")
