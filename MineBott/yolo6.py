from scraper2 import getpage

start_letters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
comp_db = dict()
data = open("comp_db.text","w")
datacsv = open("comp_db.csv","w")
def name_adder(letter):
    url = 'https://www.moneycontrol.com/india/stockpricequote/'+letter
    page = getpage(url)
    table = page.find('table', {'class': 'pcq_tbl MT10'})
    for col in table.find_all('td') :
        key = col.get_text().lower()
        value = col.a.attrs['href']
        comp_db[key] = value
        data.write(key + "  :  " + value)
        datacsv.write(key + " , " + value)
        data.write("\n")
        datacsv.write("\n")


for i in start_letters:
    name_adder(i)

name_adder('others')
data.close()
datacsv.close()
