from forumDB.functions.database import exec_insert_update_delete_query
import MySQLdb as mDB
__author__ = 'maxim'

host = 'localhost'
user = 'maxim'
password = '12345'
database = 'forumDB_ID'

def create_forum(required_params):
    db = mDB.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()

    query = """select id from Users where email = %s """
    cursor.execute(query, (required_params['user'], ))
    id = cursor.fetchone()[0]

    id = exec_insert_update_delete_query('insert into Forums (name , short_name , user, u_id ) values (%s , %s , %s, %s )',
                                         (required_params['name'], required_params['short_name'],
                                          required_params['user'], id ,))
    return {
        'name': required_params['name'],
        'short_name': required_params['short_name'],
        'user': required_params['user'],
        'id': id
    }
