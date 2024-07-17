a = int(input())
b = int(input())
if a < b:
    odd_numbers = [i for i in range(a, b + 1) if i % 2 != 0]
    print(*odd_numbers)
else:
    odd_numbers = [i for i in range(a, b - 1, -1) if i % 2 != 0]
    print(*odd_numbers)