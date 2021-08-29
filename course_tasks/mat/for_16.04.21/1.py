import random


def max_age(data):
    max_age_p = 0

    for item in data:
        if max_age_p < item['age']:
            max_age_p = item['age']

    return max_age_p


def find_oldest(data):
    m_age = max_age(data)
    for item in data:
        if item['age'] == m_age:
            print(item['salary'])


def create_data(k=10):
    result = []
    while k > 0:
        result.append({
            'age': random.randint(20, 60),
            'salary': random.uniform(10000, 100000),
        })
        k -= 1

    return result


if __name__ == '__main__':
    find_oldest(create_data())
