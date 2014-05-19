from forumDB.functions.database import exec_insert_update_delete_query
from forumDB.functions.thread.getters import get_thread_details
import MySQLdb as mDB

__author__ = 'maxim'

host = 'localhost'
user = 'maxim'
password = '12345'
database = 'forumDB_ID'


def create_thread(required_params, optional_params):
    info = {
        'forum': required_params['forum'],
        'title': required_params['title'],
        'isClosed': required_params['isClosed'],
        'user': required_params['user'],
        'date': required_params['date'],
        'message': required_params['message'],
        'slug': required_params['slug']
    }
    db = mDB.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()

    cursor.execute('select id from Forums where short_name = %s',(required_params['forum'],))
    f_id = cursor.fetchone()[0]

    cursor.execute('select id from Users where email = %s',(required_params['user'],))
    u_id = cursor.fetchone()[0]

    query = 'insert into Threads (forum , title , isClosed , user , date , message , slug , f_id, u_id'
    values = '(%s, %s, %s, %s, %s, %s, %s, %s, %s '
    query_params = [required_params['forum'], required_params['title'], required_params['isClosed'],
                    required_params['user'], required_params['date'], required_params['message'],
                    required_params['slug'], f_id, u_id]
    if optional_params['isDeleted'] is not None:
        query += ' , isDeleted '
        values += ' , %s '
        query_params.append(optional_params['isDeleted'])
        info['isDeleted'] = optional_params['isDeleted']
    query += ') values ' + values + ' )'

    cursor.execute(query, query_params)
    info['id'] = cursor.lastrowid
    db.commit()

    return info


def subscribe_thread(required_params):

    db = mDB.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()

    cursor.execute('select id from Users where email = %s', (required_params['user'],))
    id = cursor.fetchone()[0]

    cursor.execute('insert into Subscriptions (user , thread, u_id) values (%s , %s, %s)',
                                    (required_params['user'], required_params['thread'], id, ))
    db.commit()
    cursor.close()
    db.close()
    return {
        'thread': required_params['thread'],
        'user': required_params['user']
    }


def unsubscribe_thread(required_params):

    db = mDB.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()

    cursor.execute('select id from Users where email = %s', (required_params['user'],))
    id = cursor.fetchone()[0]

    cursor.execute('delete from Subscriptions where u_id = %s and thread = %s',
                                    (id, required_params['thread'], ))
    db.commit()
    cursor.close()
    db.close()

    return {
        'thread': required_params['thread'],
        'user': required_params['user']
    }


def thread_vote(required_params):

    db = mDB.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()

    if required_params['vote'] == 1:
        cursor.execute(
            'update Threads set likes = likes + 1 , points = points + 1 where id = %s',
            (required_params['thread'],))
    if required_params['vote'] == -1:
        cursor.execute(
            'update Threads set dislikes = dislikes + 1, points = points - 1 where id = %s',
            (required_params['thread'],))
    db.commit()
    info = get_thread_details(required_params['thread'], None, cursor)
    cursor.close()
    db.close()
    return info


def close_or_open(type, thread):
    id = 0
    if type == 'open':
        id = exec_insert_update_delete_query('update Threads set isClosed = 0 where id = %s', (thread,))
    if type == 'close':
        id = exec_insert_update_delete_query('update Threads set isClosed = 1 where id = %s', (thread,))
    return {
        'id': id
    }


def thread_update(required_params):
    db = mDB.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()
    cursor.execute("update Threads set message = %s , slug = %s where id = %s",
                                    (required_params['message'], required_params['slug'], required_params['thread'],))
    db.commit()
    info = get_thread_details(required_params['thread'], None, cursor)
    cursor.close()
    db.close()
    return info

def thread_remove_restore(required_params, type):
    id = 0
    if type == 'remove':
        id = exec_insert_update_delete_query("update Threads set isDeleted = 1 where id = %s",
                                             (required_params['thread'],))
    if type == 'restore':
        id = exec_insert_update_delete_query("update Threads set isDeleted = 0 where id = %s",
                                             (required_params['thread'],))
    return {'thread': id}