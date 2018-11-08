import os

data = []
for file in os.listdir('./data'):
    with open('./data/{}'.format(file)) as fh:
        data += fh.readlines()

salaries = {}
for line in data:
    date, name, gender, salary, city = line.split(',')

    city = city.strip()
    gender = gender.strip().upper()

    if city not in salaries:
        salaries[city] = {}

    if gender not in salaries[city]:
        salaries[city][gender] = []

    salaries[city][gender].append(int(salary))

for city, value in salaries.items():
    print(city)
    for k, v in value.items():
        print(k)
        print(max(v), min(v), sum(v) / len(v))
