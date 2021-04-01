from random import randint

k = []
k_range = int(input('Введите кол-во элементов списка: '))
for i in range(k_range):
    k.append((randint(1, 100)))

print(k)
k.reverse()
print(k)