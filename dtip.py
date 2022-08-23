#Import libraries
import requests ,sys ,csv,json,sqlite3 ,re
from bs4 import BeautifulSoup
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
import html5lib
import threading


class Check_start(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def create_divar_tables(self):
        try:
            sqliteConnection = sqlite3.connect('brantipdivar.db')
            sql_divar_brand = '''CREATE TABLE divrbarnd (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT ,
                                    brand TEXT 
                                    );'''
            sqli_divr_model = '''CREATE TABLE divarmodel (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT  ,
                                    brand_id REFERENCES divrbarnd(id)  ,
                                    model TEXT );'''
            sqli_divr_tip = '''CREATE TABLE divartip (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT  ,
                                    model_id REFERENCES divarmodel(id)  ,
                                    tip TEXT );'''
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sql_divar_brand)
            sqliteConnection.commit()
            cursor.execute(sqli_divr_model)
            sqliteConnection.commit()
            cursor.execute(sqli_divr_tip)
            sqliteConnection.commit()
            print("SQLite tables created")
            cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def insert_divar_brand(self, brand):
        try:
            sqliteConnection = sqlite3.connect('brantipdivar.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO divrbarnd
                                            (brand) 
                                            VALUES (?);"""

            data_tuple = (brand, )
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into divrbarnd table")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def delete_chat_id(self, id):
        try:
            sqliteConnection = sqlite3.connect('brantipdivar.db')
            cur = sqliteConnection.cursor()
            sql = 'DELETE FROM chats WHERE chat_id=?'

            cur.execute(sql, (id,))
            sqliteConnection.commit()

        except sqlite3.Error as error:
            print("Failed to delete from table ", error)

    def readBrand(self):
        try:
            sqliteConnection = sqlite3.connect('brantipdivar.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sqlite_select_query = """SELECT * from divrbarnd"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()

            cursor.close()
            return records

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def find_one(self, chid):
        try:
            sqliteConnection = sqlite3.connect('brantipdivar.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql = 'SELECT chat_id from chats WHERE chat_id=?'
            cursor.execute(sql, (chid,))
            records = cursor.fetchall()

            cursor.close()
            return records

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

sqliobj = Check_start ()
# sqliobj.create_divar_tables()




# brands = sqliobj.readBrand()

# for brand in brands:
#     print(brand[1])













myFile=open('divar.html','r',encoding='utf-8')
soup=BeautifulSoup(myFile,"html5lib")


all_scripts = soup.find('script')
script = str(all_scripts)
# print(all_scripts[7])

# data = re.search(r"window\.\_\_PRELOADED\_STATE\_\_ \=", script)


data = json.loads(str(script[43:]))
print(data)
# data = json.dumps(data, indent=4)
# print(data)
i = 0
try:
    
    with open('Test.csv',"a+",encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        row = script[43:]
        writer.writerow(row)
        csv_file.close()
    i = i + 1
except:
    pass


# for script in soup('script'):
#     span = script.extract()
#     try:
#         print (span)
#         with open('Test.csv',"a+", newline='',encoding='utf-8') as csv_file:
#             writer = csv.writer(csv_file)
#             row = [str(span),i]
#             writer.writerow(row)
#             csv_file.close()
#         i = i + 1
#     except:
#         pass



# for script in soup("script"):

#     try:
#         span = script.extract()
#         print (span)
#         with open('Test.csv',"a+", newline='',encoding='utf-8') as csv_file:
#             writer = csv.writer(csv_file)
#             row = [span,i]
#             sqliobj.insert_divar_brand(span.strip())
#             writer.writerow(row)
#             csv_file.close()
#         i = i + 1
#     except:
#         pass


# response = requests.get('https://www.sheypoor.com/ایران/وسایل-نقلیه/خودرو', headers=headers)
# soup = BeautifulSoup(response.content,"html.parser")

# i = 1
# for el in soup.find_all("li",class_="kt-internal-link-list__item internal-link-item"):
#     try:
#             # print(el)
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

# page = requests.get("https://divar.ir/s/tehran/car/")
# soup = BeautifulSoup(page.content,"html.parser")

# i = 1
# for el in soup.find_all("div", "multi-select-modal__list"):
#     span = el.find("p").get_text()
#     print(span)
#     with open('ImplementTest.csv',"w", newline='',encoding='utf-8') as csv_file:
#         writer = csv.writer(csv_file)
#         row = [span, i]
#         writer.writerow(row)
#         csv_file.close()
#     i = i + 1