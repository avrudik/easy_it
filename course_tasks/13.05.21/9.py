import openpyxl as xl

with open('9.txt', 'r') as f:
    file_content = f.read().split('\n')

my_list = [i.split(',')[-4:-1] for i in file_content][1:]
print(my_list)
my_dict = {}
cities = []
jobs = []
# for item in file_content:
#     cities.append(item[-4])
#     jobs.append(item[-3])
