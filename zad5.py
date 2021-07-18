

profit = float(input('Введите сумму выручки за год: '))
costs = float(input('Введите сумму издержек за год: '))
if profit > costs:
    print(f'Поздравляю! Вы не банкрот. Рентабельность выручки составила {(profit / (profit - costs)):.2f}')
    workers = int(input('Введите количество сотрудников: '))
    print(f'Ваша прибыль на одного сотрудника составила: {profit / workers:.2f}')
elif profit == costs:
    print('Целый 0 выручки за год, кажется, это успех')
else:
    print('Ваш корабль идет ко дну...')
