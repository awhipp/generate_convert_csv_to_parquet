import sys
import csv
import os
import pandas as pd
from faker import Faker

fake = Faker()
number_of_records = int(sys.argv[1])

# Check whether the specified path exists or not
isExist = os.path.exists('data')

if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs('data')
  print('Data folder created.')

with open('./data/birth_dates.csv', mode='w', newline='', encoding='utf-8') as file:
  file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

  file_writer.writerow(['first_name', 'last_name', 'year', 'month', 'day'])

  for _ in range(number_of_records):
    date = fake.date().split('-')
    year = date[0]
    month = date[1]
    day = date[1]

    file_writer.writerow([fake.first_name(), fake.last_name(), year, month, day])

print('CSV file generated.')

df = pd.read_csv('./data/birth_dates.csv')
df.to_parquet('./data/birth_dates', compression='snappy', partition_cols=['year', 'month'])
print('Partitioned Parquet generated.')