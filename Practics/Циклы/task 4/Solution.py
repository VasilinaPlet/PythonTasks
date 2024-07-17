n = int(input())

# считываем числа в последовательности и фильтруем четные числа
even_numbers = list(filter(lambda x: x % 2 == 0, [int(input()) for _ in range(n)]))

# считаем сумму четных чисел и количество четных чисел
even_sum = sum(even_numbers)
even_count = len(even_numbers)

# вычисляем среднее арифметическое четных чисел и выводим его на экран
print(even_sum / even_count)