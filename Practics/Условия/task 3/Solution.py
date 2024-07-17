a = int(input())
if a % 10 == 1 or a // 10 % 10 == 1 or a // 100 == 1:
    print("Да")
else:
    print("Нет")