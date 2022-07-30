#Import libraries
import requests ,sys ,csv

from bs4 import BeautifulSoup
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
#Request URL
page = requests.get("https://asemooni.com/tehran-regions-21458")

#Fetch webpage
soup = BeautifulSoup(page.content,"html.parser")

#Scraping Data
i = 1
for el in soup.find_all("li"):
    print(el.get_text())
    with open('ImplementTest.csv',"w", newline='',encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        row = [el.get_text(), i]
        writer.writerow(row)
        csv_file.close()
    i = i + 1