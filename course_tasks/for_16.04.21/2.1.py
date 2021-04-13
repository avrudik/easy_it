K = int(input("Enter student's number: "))


def func(n):
    if n <= 0:
        return 0

    elif n == 1:
        return 1

    else:
        return func(n-2) + (K*K - 1) * func(n-1)


if __name__ == '__main__':
    print(func(int(input('Now enter n: '))))
