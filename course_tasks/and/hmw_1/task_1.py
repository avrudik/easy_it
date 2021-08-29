from random import randint

print([i for i in [randint(-1000, 1000) for i in range(int(input('Please enter a number of elements: ')))] if i % 2 == 0])
