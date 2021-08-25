import openpyxl as xl


with open('3.txt', 'r') as f:
    s = f.read().split('\n')

s = [i.split(',') for i in s]
teachers = [i for i in s if i[-3] == 'учитель']

# City, average, median
my_dict = {}
for person in teachers:
    city = person[-4]
    salary = person[-2]
    my_dict[city] = my_dict[city] + [int(salary)] if city in my_dict else []

for i in my_dict:
    list_of_salaries = my_dict[i]
    list_of_salaries.sort()
    average = round(sum(list_of_salaries)/len(list_of_salaries), 2)
    length = len(list_of_salaries)
    median = round(list_of_salaries[length//2 - 1] + list_of_salaries[length//2], 2) if length % 2 == 0 else \
        list_of_salaries[length//2]
    my_dict[i] = [average, median]

max_val = ['', 0, 0]
for i in my_dict:
    if my_dict[i][1] >= max_val[2]:
        max_val = [i] + my_dict[i]


city = max_val[0]
average = max_val[1]
median = max_val[2]
print(f'В городе {city} живут самые богатые учителя: медиана = {median}, средняя з/п = {average}')

wb = xl.Workbook()
sheet = wb.active
sheet.title = 'Data'
for i in s:
    sheet.append(i)
wb.save('Тюменцева.xlsx')
