from random import randint

k = int(input())
some_list = []
for i in range(k):
    tmp = randint(-1000, 1000)
    if tmp % 2 == 0:
        some_list.append(tmp)

print(some_list)

