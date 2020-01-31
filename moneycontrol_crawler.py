#!/usr/bin/env python3
from scraper2 import getpage
import sys
import csv
data = []
# reading the csv file -
def compfind(file="comp_db.csv"):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)


compfind()
# taking company name input -
col = [x[0].strip() for x in data if x[0]]
name = input("enter a company name : ").lower()
if name in col:
    for x in range(0, len(data)):
        if name == data[x][0].strip():
            found = data[x]
            url = data[x][1]
else:
    print('name not found , type the full and correct name')
    sys.exit(-1)

# crawling and scraping -
comp_name =''
comp_name += found[0].strip()+'.txt'
f = open(comp_name, "+w")

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
view_more = corp_act.find('div',{'class':'viewmore'}).a.attrs['href']

# going to dividends page -
view_more = view_more.replace('board-meetings', 'dividends')
div_page = getpage(view_more)
divpage_head = div_page.find('div', {'class': 'divin_content MT20'})
for i in divpage_head.find_all('p'):
    print(i.get_text())
    f.write(i.get_text()+"\n\n")

table_head = div_page.find('table', {'class': 'mctable1'}).thead.tr
print(table_head.get_text())
f.write(table_head.get_text()+"\n")

table_body = div_page.find('table', {'class': 'mctable1'}).tbody
table_rows = table_body.find_all('tr')
for col in table_rows:
    print(col.get_text())
    f.write(col.get_text())

