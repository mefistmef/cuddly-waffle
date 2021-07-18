# принудительно бесконечный цикл
i = 0

while True:
    i += 1
    if i >= 10:
        break
    if i % 2 == 0:
        continue
    print(i)



while num <= 10:
    print(num)
    # num = num + 1
    num = += 1