import math


def issimple(n):
    r = math.ceil(math.sqrt(n))
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = 5
s = [2, 3]
while True:
    if issimple(n) is True:
        s.append(n)
    if len(s) == 10001:
        break
    n += 2

print(s[-1])