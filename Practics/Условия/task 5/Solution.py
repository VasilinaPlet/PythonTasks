month = int(input())
if month == 1 or month == 2 or month == 12:
    print("Зима")
if month >= 3 and month <= 5:
    print("Весна")
if month >= 6 and month <=8:
    print("Лето")
if month >= 9 and month <=11:
    print("Осень")
if month > 12 or month < 1:
    print("Неверный номер месяца")