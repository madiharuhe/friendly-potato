import csv

with open('enjoysport.csv', 'r') as file:
    data = list(csv.reader(file))

hypothesis = data[1][:-1]
for row in data[1:]:
    if row[-1] == 'yes':
        hypothesis = [h if h == v else '?' for h, v in zip(hypothesis, row[:-1])]

print(hypothesis)
