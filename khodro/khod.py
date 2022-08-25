import requests ,sys ,csv,json,sqlite3 ,re
from bs4 import BeautifulSoup
from database import Check_start

obj =  Check_start()
obj.create_khodro_tables()


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

f = open('shaypoor_brand.json',encoding='utf-8')
data = json.load(f)

url = 'https://khodro45.com/api/v2/car_listing/?ordering=-created_time&brand_url_slug='

def getdata(my_req_url):
    response = requests.get(my_req_url)
    response_dict = json.loads(response.text)
    return response_dict

brand = ""
for i in data['Brand']:
    brand = i['title_en']
    req_url = url + brand.lower()
    # obj.insert_khodro_brand(i['title'],req_url )
    page_data = getdata(req_url)
    for car_data in page_data['results']:
        obj.insert_khodro_model(i['title'],car_data['car_properties']['model']['title'],car_data['car_properties']['trim'])
    if page_data['next']:
        next_page_data = page_data['next']
        page_data = getdata(next_page_data)
        for car_data in page_data['results']:
            obj.insert_khodro_model(i['title'],car_data['car_properties']['model']['title'],car_data['car_properties']['trim'])

f.close()

# print(brand.lower())




# page_data = getdata(req_url)

# if page_data['next']:
#     next_page_data = getdata(page_data['next'])
# else:
#     next_page_data = None
# print(next_page_data)






