import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.realitica.com/'
num_pages = int(input("Add number of pages you want to search?"))

links = []
for page_num in range(1, num_pages + 1):  # zamijenite num_pages s brojem stranica koje želite pretražiti
    response = requests.get(f'{url}/pretraga/novo/1/1/{page_num}/')
    soup = BeautifulSoup(response.text, 'html.parser')
    link_divs = soup.find_all('div', class_='thumb_div')
    for link_div in link_divs:
        link = link_div.find('a')['href']
        links.append(link)

with open('realitica_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['vrsta', 'područje', 'lokacija', 'broj_spavaćih_soba', 'broj_kupatila', 'cijena', 'stambena_površina', 'zemljište', 'parking_mjesta', 'od_mora', 'novogradnja', 'klima', 'naslov', 'opis', 'web_stranica', 'oglasio', 'mobilni', 'broj_id_oglasa', 'zadnja_promjena', 'slike']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Skrejpovanje potrebnih podataka
        # ...
        
        # Pisanje podataka u CSV
        writer.writerow({'vrsta': ...})  
