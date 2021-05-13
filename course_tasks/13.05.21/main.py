with open('17.txt', 'r') as f:
    s = f.read().split('\n')

my_dict = {}
all_people_num = len(s)
for item in s:
    if s.index(item) != 0:
        prof = item.split(',')[-3]
        my_dict[prof] = my_dict[prof] + 1 if prof in my_dict else 1

for profession in my_dict:
    percentage = my_dict[profession]/all_people_num
    print(f'{profession.title()} - {my_dict[profession]} ({round(percentage, 2)}%)')
