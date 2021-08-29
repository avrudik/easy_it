from random import randint

k = int(input('Enter a list length: '))
some_list = [randint(1, 1000) for i in range(k)]

if len(some_list) % 2 == 0:
    print(sum(some_list))
else:
    print(some_list[len(some_list)//2])
