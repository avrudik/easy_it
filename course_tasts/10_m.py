people = [

    {

        "fullname": "Jill Gold",

        "age": 24,

        "single": False,

        "salary": 80000

    },

    {

        "fullname": "Tracy Harrell",

        "age": 27,

        "single": True,

        "salary": 60000

    },

    {

        "fullname": "Faye Kinney",

        "age": 30,

        "single": False,

        "salary": 90000

    },

    {

        "fullname": "Edgar Russell",

        "age": 43,

        "single": False,

        "salary": 120000

    },

    {

        "fullname": "Hilda Stephens",

        "age": 31,

        "single": False,

        "salary": 105000

    },

    {

        "fullname": "Barry Walton",

        "age": 26,

        "single": False,

        "salary": 50000

    },

    {

        "fullname": "Willie Paul",

        "age": 37,

        "single": True,

        "salary": 98000

    },

    {

        "fullname": "Lewis Barton",

        "age": 29,

        "single": False,

        "salary": 115000

    },

    {

        "fullname": "Katherine Hamilton",

        "age": 33,

        "single": True,

        "salary": 113000

    },

    {

        "fullname": "Miriam Puckett",

        "age": 41,

        "single": False,

        "salary": 98000

    }

]

salaries = []
ages = []
family = []
name = str()
salary_amount = 0
i = 0
for item in people:
    if item['salary'] > salary_amount:
        salary_amount = item['salary']
        name = item['fullname']
    salaries.append(item['salary'])
    ages.append(item['age'])
    if item['single']:
        i += 1

print(f'Человек с самой большой зарплатой ({salary_amount}) - {name}')
print(f'Средний возраст людей: {sum(ages) / len(ages)}')
print(f'Средняя зарплата людей: {sum(salaries) / len(salaries)}')
print(f'Кол-во людей без пары: {i}')

