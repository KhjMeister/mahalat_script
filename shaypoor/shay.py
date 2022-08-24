from database import Check_start
import requests ,sys ,csv,json,sqlite3 ,re
from bs4 import BeautifulSoup
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
import html5lib
import threading

obj =  Check_start()
# obj.create_shay_tables()
# brands = obj.readBrand()


# headers = {
# 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
# 'Accept-Encoding' : 'gzip, deflate, br',
# 'Accept-Language' :	'en-US,en;q=0.5',
# 'Connection' :	'keep-alive',
# 'Cookie' :	'searchKey=eyJfdXJsIjoic2VhcmNoIiwiYnJhbmRJblNsdWciOiI0Mzk3MyIsImMiOiI0Mzk3MyJ9; ts=3ddbb6fc19859bc76c6479ceef44a470; track_id=0f6e27bd032033e0c07a11523d795313; _ga=GA1.2.918465674.1661102035; _gid=GA1.2.1931799951.1661102035; geo=dont-care; AMP_TOKEN=%24NOT_FOUND',
# 'Host' :	'www.sheypoor.com',
# 'Sec-Fetch-Dest' :	'document',
# 'Sec-Fetch-Mode' :	'navigate',
# 'Sec-Fetch-Site' :	'cross-site',
# 'Upgrade-Insecure-Requests' :	'1',
# 'User-Agent' :	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
# }

# for brand in brands:
    # response = requests.get(str(brand[2]),allow_redirects=False,headers=headers)
    # soup = BeautifulSoup(response.content,"html.parser")

    # for el in soup.find_all("a",class_="blue"):
    #     try:
    #         span = el.find('span',class_="title")
    #         # print(str(brand[1]),span.text.strip())
    #         obj.insert_shay_model(brand[0],span.text.strip(),span.text.strip())

    #     except:
    #         pass


# brands = obj.readmodel()

# for brand in brands:
#     b = brand[2] 
#     b=re.sub("\(.*?\)","",b)
#     obj.update_model(brand[0] ,b)
#     print(brand[2])

brands = obj.readBrand()
models = obj.readmodel()

for brand in brands:
    for model in models:
        if brand[0]==model[1]:
            obj.update_model(brand[1] ,model[1])
   