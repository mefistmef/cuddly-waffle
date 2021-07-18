# Узнайте у пользователя число n. Найдите сумму n+nn+nnn.
# Например, пользователь ввел 3, 3+33+333=369.

namber = (input('Введите число: '))

x = int(namber) + int(namber + namber) + int(namber + namber + namber)
print(x)
