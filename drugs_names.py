from bs4 import BeautifulSoup
import requests 
import csv


csv_file = open('leki.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['leki'])






source2 = requests.get('https://www.lekinfo24.pl/').text
soup2 = BeautifulSoup(source2, 'lxml')
drug_all = []


for offer2 in soup2.find_all('div',class_ = 'lsInner d-flex w-100 flex-md-nowrap flex-wrap'):
        for offer3 in offer2.find_all('a', href=True):
            drb = ('https://www.lekinfo24.pl' + offer3['href'])
            dwg =drug_all.append(drb)
for x in drug_all:
    source3 = requests.get(x).text
    soup3 = BeautifulSoup(source3, 'lxml')
    for offer4 in soup3.find_all('div',class_ = 'col-md-9 left-content'):
        for dr in offer4.find_all('ul', class_=True):
            for drA in dr.find_all('a', href=True):
                print(drA.text)
                csv_writer.writerow([drA])
csv_file.close()
    



   