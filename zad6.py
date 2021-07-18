a = int(input('Введите результат первого дня, (км): '))
b = int(input('Введите необходимый результат: '))
rez_day = 1

while a < b:
    a *= 1.1
    rez_day += 1

print(rez_day)
