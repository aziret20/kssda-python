import os

lines = []
for file in os.listdir('./data'):
    with open('./data/{}'.format(file)) as fh:
        lines += fh.readlines()

salaries = []
for line in lines:
    date, name, gender, salary, city = line.split(',')
    salaries.append(int(salary))

# print(max(salaries), min(salaries), sum(salaries) / len(salaries))

#
# # Open file
# with open('data.csv') as fh:
#     lines = fh.readlines()
#
# # Read file
# for line in lines:
#     date, name, city = line.split(',')
#     day, month, year = date.split('.')
#
#     if not os.path.exists(year):
#         os.mkdir(year)
#
#     with open('{year}/data.csv'.format(year=year), 'a') as fh:
#         fh.write(line)
