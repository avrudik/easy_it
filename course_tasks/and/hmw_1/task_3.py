def do_it(data, sub):
    data = data[data.find(sub) + len(sub):]
    return 1, data

input_str = input('Input some string: ')
sub_str = input('Input a sub-string: ')
answer = 0
while input_str and sub_str in input_str:
    sum, input_str = do_it(input_str, sub_str)
    answer += sum
else:
    print('String is over or there is no sub-string in initial string.')

print(answer)
