from database import Check_start

obj =  Check_start

brands = obj.readBrand()

for brand in brands:
    print(brand[2])


# response = requests.get('https://www.sheypoor.com/ایران/وسایل-نقلیه/خودرو', headers=headers)
# soup = BeautifulSoup(response.content,"html.parser")

# i = 1
# for el in soup.find_all("li",class_="kt-internal-link-list__item internal-link-item"):
#     try:
#             print(el)
#             span = el.a.h2.text
#             with open('Test.csv',"a+", newline='',encoding='utf-8') as csv_file:
#                 writer = csv.writer(csv_file)
#                 row = [span.strip(), i]
#                 sqliobj.insert_divar_brand(span.strip())
#                 writer.writerow(row)
#                 csv_file.close()
#             i = i + 1
#     except:
#         pass