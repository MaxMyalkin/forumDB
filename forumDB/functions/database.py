__author__ = 'maxim'
import MySQLdb as mdb

host = 'localhost'
user = 'maxim'
password = '12345'
database = 'forumDB'

def exec_clear(query, params):
    db = mdb.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0', [])
    cursor.execute(query, params)
    cursor.execute('SET FOREIGN_KEY_CHECKS=1', [])
    db.commit()
    cursor.close()
    db.close()


def exec_insert_update_delete_query(query, params):
    db = mdb.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()
    last_id = cursor.lastrowid
    cursor.close()
    db.close()
    return last_id


def exec_select_query(query, params):
    db = mdb.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
