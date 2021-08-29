from math import *
from random import randint

table = '''1
1, 1, 1
10
1, 3, 4
19
1, 2, 7
2
2, 2, 1
11
2, 1, 4
20
2, 3, 7
3
3, 3, 1
12
3, 2, 4
21
3, 1, 7
4
4, 1, 2
13
4, 3, 5
22
4, 2, 8
5
5, 2, 2
14
5, 1, 5
23
5, 3, 8
6
6, 3, 2
15
6, 2, 5
24
6, 1, 8
7
7, 1, 3
16
7, 3, 6
25
7, 2, 9
8
8, 2, 3
17
8, 1, 6
26
8, 3, 9
9
9, 3, 3
18
9, 2, 6
27
9, 1, 9'''.split('\n')
table = {
    int(student_num): [*map(int, tasks.split(', '))] for student_num, tasks in zip(table[0::2], table[1::2])
}


def z_func(x, k, g, f, h):
    g_funcs = {
        1: lambda k_: 1/(factorial(k) * (2*k_ + 1)),
        2: lambda k_: (k_*k_ - k_)/factorial(k_+1),

    }

    return g_funcs[2](k)


def student_connect(k):
    return table[k]


if __name__ == '__main__':
    student_number = int(input('Please enter your student number in home.mephi list: '))
    tasks = student_connect(student_number)
    x = randint(log(student_number + 1), 2 * student_number)
    print(f'Numbers of tasks for you are: ', end='')
    print(*tasks, sep=', ')
    print(z_func(x, student_number, 1, 1, 1))
