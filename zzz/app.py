
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

    def insert_chats(self, mapir, lng, lat):
        try:
            sqliteConnection = sqlite3.connect('data.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO Chats
                                            (mapir, lng,lat) 
                                            VALUES (?, ?,?);"""

            data_tuple = (mapir, lng, lat)
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
            "Content-Type": "application/json",
            "x-api-key": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjMzMzBkZjMxZDIxYTZjMmE4MjMzODg3OGQyMTAyZTY2MmZiYTg2MjJlYzA4ZWQ3OWE0NTU1YTE2Mjg2ZjllYWQxODMyNWMxMDY2MWZlYTdmIn0.eyJhdWQiOiIxODgzNSIsImp0aSI6IjMzMzBkZjMxZDIxYTZjMmE4MjMzODg3OGQyMTAyZTY2MmZiYTg2MjJlYzA4ZWQ3OWE0NTU1YTE2Mjg2ZjllYWQxODMyNWMxMDY2MWZlYTdmIiwiaWF0IjoxNjU4NTYzOTM0LCJuYmYiOjE2NTg1NjM5MzQsImV4cCI6MTY2MTE1NTkzNCwic3ViIjoiIiwic2NvcGVzIjpbImJhc2ljIl19.AsxIUuCllm6d_lJOr190MSOlSZUYPRhsgcgRYDp2yoABWVdu7m_DZD7uhOl_4oguyazOk-cqjaEkARvb6knWOqR9vhxvGSvLqWuCkaBE4MBzUWLKGPyzEpvNfqjBlTXivGJgNY9WH08XDLoP8ggCqJvf6z2O35s07H4fypeCj_9o35zMSjlRbBQ7C7HUx56ZKVh3Z0Syji7xF0yWTR8pWGvjPRjGgXs3YkrdfJKNwAgggdxkxBva898XSbefTXRaKv4Svxl5q0-w_WB5a3Iw6iRWC6PclASpoxMySpqCWPIxVEjC80nmWqfIXDiP6_ptWU8BX0a8-qrgBNw2ulWRPg"
        }

    def postRequest(self, requ):

        response = requests.post(url, json={
                                 'text': requ, "$select": 'neighborhood', "$filter": 'province eq ??????????'}, headers=self.headers)
        response_dict = json.loads(response.text)
        return response_dict


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

sqlit_obj = SqliteDataBase()
# sqlit_obj.create_chats_table()
neighbor_obj = Neighbors()
# response = sqliobj.postRequest("???????????? ?????????? 16")
# print(response['value'][0]['geom']['coordinates'])
# sqliobj.insert_chats('5113619438','09050944668')


# fcc_file = open('neighbourhoods_tehran.json', 'r', encoding='utf-8')
# fcc_data = json.load(fcc_file)
# print(fcc_data)
results = sqlit_obj.readSqliteTable()
lat = ''
lang = ''
for data in results:

    try:
        respons = neighbor_obj.postRequest(data[0])
        neighbor = data[0]
        print(respons)
        lat = respons['value'][0]['geom']['coordinates'][0]
        lang = respons['value'][0]['geom']['coordinates'][1]

        sqlit_obj.update_requ(
            neighbor, lat, lang)
        
  
    except:
        pass
