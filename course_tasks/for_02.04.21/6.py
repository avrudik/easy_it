from random import randint

k_range = int(input('Введите кол-во элементов списка: '))
k = [randint(1, 10) for i in range(k_range)]
m = int(input('Введите число m: '))
n = 0
for item in k:
    if m == item:
        n += 1

print(f'Число m встречается в списке {n} раз')
