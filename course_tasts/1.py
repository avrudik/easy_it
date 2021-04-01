number_list = [i for i in range(1, 1000)]
number_list_k = []
for item in number_list:
    if item % 3 == 0 or item % 5 == 0:
        number_list_k.append(item)

print(number_list_k)