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

people.sort(key=lambda x: x['salary'])
print(f'Человек с само большой зарплатой - {people[-1]["fullname"]}')
print(f'Средняя зарплата - {sum([i["salary"] for i in people])/len(people)}')
print(f'Средний возраст - {sum([i["age"] for i in people])/len(people)}')
print(*[i['fullname'] for i in people if i['single']], sep=', ')
