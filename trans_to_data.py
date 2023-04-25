import csv

l = []
with open('output.csv',newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        l.append(row[0])


file = open('items.txt','w')
file.write(f'data = [')
for el in l:
    file.write(f'"{el}",')
file.write(f']')
