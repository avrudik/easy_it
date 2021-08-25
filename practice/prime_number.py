def prime_number(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num


if __name__ == '__main__':
    n = int(input('Введите число: '))
    print(prime_number(n))
