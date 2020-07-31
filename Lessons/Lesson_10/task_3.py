import csv, sys
from importlib import reload
reload(sys)
sys.setdefaultencoding('utf-8')
with open('test.csv', 'r') as csvf:
    csvread = csv.reader(csvf)
    for row in csvread:
        print(row)
rows = [
    ['Ivan', 'Ivanov', 'Z-23'],
    ['Petr', 'Petrov', 'Z-23'],
]
filename = "json_file.JSON"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)  # запишет одну строку