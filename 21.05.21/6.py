import openpyxl
book = openpyxl.load_workbook('variant_6.xlsx')

path = 'D:\Easy_it_github\easy_it\21.05.21\variant_6.xlsx'
sheet = book.active
data = sheet['A2':'E1001']
print(data)
for i in data:
    print(i[0].value.split())