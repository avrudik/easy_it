three_digit_numbers = [i for i in range(100, 1000)]
lst = []
for item in three_digit_numbers:
    for i in three_digit_numbers:
        a = item * i
        b = list(str(a))
        if len(b) % 2 == 0:
            if b[: len(b)//2] == b[len(b)//2:][::-1]:
                lst.append(a)
print(max(lst))