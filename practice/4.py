num = input('Введите число: ')
num = num if int(num) >= 0 else num[1:]
print(sum([int(i) for i in num]))
