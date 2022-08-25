
import sqlite3 

# sys.stdin.reconfigure(encoding='utf-8')
# sys.stdout.reconfigure(encoding='utf-8')

import threading


class Check_start(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def create_divar_tables(self):
        try:
            sqliteConnection = sqlite3.connect('brandtipdivar2.db')
            sql_shay_brand = '''CREATE TABLE divarbrand (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT ,
                                    brand TEXT 
                                    );'''
            sqli_shay_model = '''CREATE TABLE divarmodel (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT  ,
                                    brand TEXT  ,
                                    model TEXT,
                                    tip TEXT );'''

            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sql_shay_brand)
            sqliteConnection.commit()
            cursor.execute(sqli_shay_model)
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
            sqliteConnection = sqlite3.connect('brandtipdivar.db')
            cursor = sqliteConnection.cursor()
            # print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO divarbrand
                                            (brand) 
                                            VALUES (?);"""

            data_tuple = (brand, )
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            # print("Python Variables inserted successfully into divarbrand table")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
    def insert_divar_model(self, brand,model,tip):
        try:
            sqliteConnection = sqlite3.connect('brandtipdivar2.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO divarmodel
                                            (brand,model,tip) 
                                            VALUES (?,?,?);"""

            data_tuple = (brand,model,tip )
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into model table")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def delete_chat_id(self, id):
        try:
            sqliteConnection = sqlite3.connect('brantipshay.db')
            cur = sqliteConnection.cursor()
            sql = 'DELETE FROM chats WHERE chat_id=?'

            cur.execute(sql, (id,))
            sqliteConnection.commit()

        except sqlite3.Error as error:
            print("Failed to delete from table ", error)

    def readBrand(self):
        try:
            sqliteConnection = sqlite3.connect('brantipdivar1.db')
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
    def readmodel(self):
        try:
            sqliteConnection = sqlite3.connect('brandtipdivar.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sqlite_select_query = """SELECT * from divarmodel"""
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
    def find_one(self, url):
        try:
            sqliteConnection = sqlite3.connect('brandtipdivar1.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql = 'SELECT id from divarbrand WHERE url=?'
            cursor.execute(sql, (url,))
            records = cursor.fetchall()

            cursor.close()
            return records

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
    def update_model(self, b_brand,bid):
        try:
            sqliteConnection = sqlite3.connect('brandtipdivar1.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql = ''' UPDATE divarmodel
                      SET brand_id = ? 
                      WHERE brand_id = ?'''

            cursor.execute(sql,(b_brand ,bid))
            sqliteConnection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")