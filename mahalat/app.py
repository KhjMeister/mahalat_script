
import sqlite3
import threading
import requests
import sys
import json
import re
url = "https://map.ir/search/v2"


class SqliteDataBase(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def create_chats_table(self):
        try:
            sqliteConnection = sqlite3.connect('data.db')
            sqlite_create_table_query = '''CREATE TABLE chats (
                                            mapir text UNIQUE,
                                            lng text,
                                            lat text,
                                            neshan text  );'''

            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")
            cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def insert_chats(self, mapir, lng, lat,neshan):
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO Chats
                                            (mapir, lng,lat,neshan) 
                                            VALUES (?, ?,?,?);"""

            data_tuple = (mapir, lng, lat,neshan)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into chats table")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
    def insert_neghbor(self, mapir, neshan):
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO Chats
                                            (mapir,neshan) 
                                            VALUES (?, ?);"""

            data_tuple = (mapir,neshan)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into chats table")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def delete_requ(self, requ):
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cur = sqliteConnection.cursor()
            sql = 'DELETE FROM chats WHERE mapir=?'

            cur.execute(sql, (requ,))
            sqliteConnection.commit()

        except sqlite3.Error as error:
            print("Failed to delete from table ", error)

    def update_requ(self, requ,lng,lat):
        try:
            sqliteConnection = sqlite3.connect('data_balad_lst.db')
            cur = sqliteConnection.cursor()
            sql = 'UPDATE chats SET lng=?, lat=? WHERE neibor=?'

            cur.execute(sql, (lng,lat,requ))
            sqliteConnection.commit()

        except sqlite3.Error as error:
            print("Failed to delete from table ", error)
    
    def readSqliteTable(self):
        try:
            sqliteConnection = sqlite3.connect('data_balad_lst.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sqlite_select_query = """SELECT * from chats"""
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


class Neighbors(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.headers = {
            "Content-Type": "application/json"
        }
    def getcitys(self):

        response = requests.get(f"https://search.raah.ir/v4/region-card/tehran/", headers=self.headers)
        response_dict = json.loads(response.text)
        return response_dict

    def getneighbors(self,city):

        response = requests.get(f"https://search.raah.ir/v4/region-card/{city}/", headers=self.headers)
        response_dict = json.loads(response.text)
        return response_dict
    def getcenter(self,city,req):

        response = requests.get(f"https://search.raah.ir/v4/region-card/{city}/{req}/", headers=self.headers)
        response_dict = json.loads(response.text)
        return response_dict


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

sqlit_obj = SqliteDataBase()
sqlit_obj.create_chats_table()

neighbor_obj = Neighbors()

results = neighbor_obj.getcitys()


for i in results['description']['data']:
    try:
        if i['slug']['city']!='tehran':
            city = i['slug']['city']
      
            result = neighbor_obj.getneighbors(city)
            
            for j in result['description']['data']:
                try:
                    res=neighbor_obj.getcenter(city,j['slug']['neighborhood'])
                    # sqlit_obj.insert_neghbor(j['slug']['neighborhood'],j['text'])
                    sqlit_obj.insert_chats(j['slug']['neighborhood'],res["center_point"][0],res["center_point"][1],j['text'])
                    
                except:
                    pass
            
    except:
        pass




# print(results['description']['data'])

# for i in results['description']['data']:
#     try:
#         if i['slug']['city']=='tehran':

#             res=neighbor_obj.getcenter(i['slug']['neighborhood'])
#             print(res["center_point"])
#             sqlit_obj.insert_chats(i['slug']['neighborhood'],res["center_point"][0],res["center_point"][1],i['text'])
#     except:
#         pass