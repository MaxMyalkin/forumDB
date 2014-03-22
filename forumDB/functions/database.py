__author__ = 'maxim'
import MySQLdb as mdb

class Database:
    host = 'localhost'
    user = 'maxim'
    password = '12345'
    database = 'forumDB'
    db = mdb.connect(host , user , password , database,init_command='SET NAMES UTF8')

def execInsertUpdateQuery(query, params):
    with Database.db:
        cursor = Database.db.cursor()
        cursor.execute(query,params)
        cursor.close()

def execSelectQuery(query, params):
    with Database.db:
        cursor = Database.db.cursor()
        cursor.execute(query,params)
        result = cursor.fetchall()
        cursor.close()
        return result