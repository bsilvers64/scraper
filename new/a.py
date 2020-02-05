#!/usr/bin/env python3
from scraper2 import getpage
import sys
import csv
import csv2json
data = []
# reading the csv file -


def compfind(file="comp_db.csv"):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)


compfind()
temp = []
# taking company name input -
col = [x[0].strip() for x in data if x[0]]
name = input("enter a company name : ").lower()
if name in col:
    for x in range(0, len(data)):
        if name in data[x][0]:
            temp.append(data[x])
else:
    print('name not found , type the full and correct name')
    sys.exit(-1)

if len(temp) > 1:
    print("multiple companies found with the same name : \n")
    print(temp)
    name = str(input("enter the specific name of the company : \n"))
    for x in range(0, len(temp)):
        if name == temp[x][0].strip():
            found = temp[x]
            url = temp[x][1]
            print(found)
else:
    found = temp[0]
    url = temp[0][1]
    print(found)

# crawling and scraping -
comp_name, comp_name2 = '', ''
comp_name += found[0].strip()+'.txt'
comp_name2 += found[0].strip()+'.csv'
f = open(comp_name, "+w")
g = open(comp_name2, "+w")


page = getpage(url)
info = page.find('div', {'class': 'main_wrapper_res corporate-wrapper'})
codes = info.find('p', {'class': 'bsns_pcst disin'}).get_text().strip('|')
codes2 = info.find_all('span', {'class': 'bsns_pcst'})
print(codes)
f.write(codes+"\n\n")
for info in codes2:
    print(info.get_text().strip('|'))
    f.write(info.get_text().strip('|')+"\n\n")


# going to corpoarte actions page -
corp_act = page.find('div', {'class': 'clearfix corportate_action'})
view_more = corp_act.find('div', {'class':'viewmore'}).a.attrs['href']

# going to dividends page -
view_more = view_more.replace('board-meetings', 'dividends')
div_page = getpage(view_more)
divpage_head = div_page.find('div', {'class': 'divin_content MT20'})
for i in divpage_head.find_all('p'):
    print(i.get_text())
    f.write(i.get_text()+"\n")


table_head = div_page.find('table', {'class': 'mctable1'}).thead.tr
rows = table_head.find_all('th')
for i in rows:
    print(i.get_text(),end=",")
    f.write(i.get_text())
    f.write(",")
    g.write(i.get_text())
    g.write(",")
print("\n")
f.write("\n")
g.write("\n")

table_body = div_page.find('table', {'class': 'mctable1'}).tbody
table_rows = table_body.find_all('tr')
for i in table_rows:
    for j in i.find_all('td'):
        f.write(j.get_text() + " , ")
        print(j.get_text(), end=" , ")
        g.write(j.get_text() + " , ")
    print("\n")
    f.write("\n")
    g.write("\n")


g.close()
f.close()
comp_name3 = comp_name2
comp_name2 = comp_name2.replace('.csv', '.json')
csv2json.convert(comp_name3, comp_name2)