lst = [i for i in range(1, 101)]
sum_of_squares = sum([i**2 for i in lst])
b = (sum(lst))**2
print(b - sum_of_squares)

