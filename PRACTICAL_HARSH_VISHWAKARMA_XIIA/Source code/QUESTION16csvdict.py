# Question 16
#to read content of student.csv

import csv
with open('student.csv') as f:
    csv_f=csv.DictReader(f)
    for row in csv_f:
        print(row)
