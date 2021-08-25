import openpyxl as xl

with open('9.txt', 'r') as f:
    file_content = f.read().split('\n')

data = {}
for i, line in enumerate(file_content):
    if i == 0:
        continue
    lastname, firstname, gender, age, height, city, job, salary, transport = line.split(",")
    job = job.strip()
    salary = int(salary.strip())
    if city not in data:
        data[city] = {}
    if job not in data[city]:
        data[city][job] = []
    data[city][job].append(salary)
checking = {'Job': 0}
for city in data:
    for prof in data[city]:
        data[city][prof] = round(sum(data[city][prof]) / len(data[city][prof]), 2)

for city in data:
    print(f'{max(data[city], key=data[city].get)} - {city} - {data[city][max(data[city], key=data[city].get)]}')


wb = xl.Workbook()
sheet = wb.active
sheet.title = 'Data'
for i in file_content:
    sheet.append(i.split(','))
wb.save('Малюкова.xlsx')
