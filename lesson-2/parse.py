import os

data = []
for file in os.listdir('./data'):
    with open('./data/{}'.format(file)) as fh:
        data += fh.readlines()

salaries = []
for line in data:
    date, name, gendre, salary, city = line.split(',')
    salaries.append(int(salary))

print(max(salaries), min(salaries), sum(salaries) / len(salaries))
