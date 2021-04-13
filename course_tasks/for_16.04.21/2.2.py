from random import randint


def func1(k):
    return [randint(0, 10000) for i in range(k)]


def func2(some_list):
    return sum(i for i in some_list if i % 2 == 1)


if __name__ == '__main__':
    print(func2(func1(100)))
