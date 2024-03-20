import csv
with open('output/walls.csv', mode ='r') as file:    
       csvFile = csv.DictReader(file)
       for lines in csvFile:
            #print(lines)
             pass

with open('output/walls.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)