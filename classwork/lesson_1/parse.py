import os
import time

start = time.time()

# Open file
with open('data.csv') as fh:
    lines = fh.readlines()

# Read file
groupped = {}
for line in lines:
    date, name, city = line.split(',')
    day, month, year = date.split('.')

    if year not in groupped:
        groupped[year] = []

    groupped[year].append(line)

for k, v in groupped.items():
    os.mkdir(k)

    with open('{year}/data.csv'.format(year=k), 'w') as fh:
        fh.write('\n'.join(v))
