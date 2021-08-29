from random import randint

answer = [randint(-1000, 1000) for i in range(int(input('Please enter a number of elements: ')))]
print([i for i in answer if i % 2 == 0])

