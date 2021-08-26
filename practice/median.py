from random import randint


def get_median(iterable):
    list_size = len(iterable)
    if len(iterable) % 2 == 0:
        return (iterable[list_size // 2 - 1] + iterable[list_size // 2]) / 2
    else:
        return iterable[list_size // 2]


k = int(input('Enter a num of elements in the list: '))
some_list = [randint(0, 1000) for i in range(k)]
some_list.sort()
print(get_median(some_list))
