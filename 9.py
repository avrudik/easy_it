def compute():
    p = 1000
    for a in range(1, p + 1):
        for b in range(a + 1, p + 1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
if __name__ == "__main__":
    print(compute())