a = input('Input smth and the program will return the type of it (except for iterable objects): ')
c = a.isdigit()
if c:
    print('int')
else:
    try:
        b = float(a)
        print('float')
    except ValueError:
        print('str')

