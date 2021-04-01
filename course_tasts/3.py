def prime_number(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

num = 600851475143
count = 2

while 1:
    if num % count == 0:
        num /= count
        print(count)
        if num == 1:
            print(count)
            break
    count += 1

