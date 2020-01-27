
import csv
import pandas as pd
data=[]
with open("a.csv",'r') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            data.append(row)

name = input("enter a file name : ").lower()

j=0
for i in data:
    i = [x.strip().lower() for x in i]
    data[j] = i
    j += 1

col= [x[0].strip() for x in data]

if name in col:
    for x in range(0, len(data)):
     if name == data[x][0]:
        print(data[x])
else:
    print("name doesn't exist")
