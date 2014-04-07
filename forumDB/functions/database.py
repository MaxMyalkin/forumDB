__author__ = 'maxim'
import MySQLdb as mdb


class Database:
    host = 'localhost'
    user = 'maxim'
    password = '12345'
    database = 'forumDB'


def execInsertUpdateQuery(query, params):
    try:
        db = mdb.connect(Database.host, Database.user, Database.password, Database.database, init_command='SET NAMES UTF8')
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        last_id = cursor.lastrowid
        cursor.close()
        db.close()
        return last_id
    except Exception:
        raise Exception('database exception')

def execSelectQuery(query, params):

        db = mdb.connect(Database.host, Database.user, Database.password, Database.database, init_command='SET NAMES UTF8')
        cursor = db.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result
