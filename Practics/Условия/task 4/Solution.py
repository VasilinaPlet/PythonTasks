a = int(input())
b = int(input())
c = int(input())
x =int(input())
if a < x and b < x or a < x and c < x or b < x and c < x:
    print("Да")
else:
    print("Нет")