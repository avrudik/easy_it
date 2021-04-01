number_list = [1, 2]
while 1:
    a = number_list[-1] + number_list[-2]
    if a < 4000000:
            number_list.append(a)
    else:
        break
print(sum([i for i in number_list if i % 2 == 0]))

