#Import libraries
import sqlite3
import threading
import requests
import sys
import json
import re
import balad
url = "https://map.ir/search/v2"

sqli_obj = balad.SqliteDataBase()

sqli_obj.create_balad_table()



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
    sqli_obj.insert_balad_neibor_data(el.get_text())
    