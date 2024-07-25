m = int(input())
a = m % 10
b = (m % 100) // 10
c = m // 100
sum = a + b + c
p = a * b * c
print("Сумма цифр =", sum)
print("Произведение цифр =", p)
