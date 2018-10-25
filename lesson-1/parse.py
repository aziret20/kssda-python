import os

# Open file
with open('data.csv') as fh:
    lines = fh.readlines()

# Read file
for line in lines:
    date, name, city = line.split(',')
    day, month, year = date.split('.')

    if not os.path.exists(year):
        os.mkdir(year)

    with open('{year}/data.csv'.format(year=year), 'a') as fh:
        fh.write(line)
