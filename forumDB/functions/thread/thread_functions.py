from forumDB.functions.database import exec_insert_update_delete_query
from forumDB.functions.thread.getters import get_thread_details

__author__ = 'maxim'


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
    query = 'insert into Threads (forum , title , isClosed , user , date , message , slug '
    values = '(%s, %s, %s, %s, %s, %s, %s '
    query_params = [required_params['forum'], required_params['title'], required_params['isClosed'],
                    required_params['user'], required_params['date'], required_params['message'],
                    required_params['slug']]
    if optional_params['isDeleted'] is not None:
        query += ' , isDeleted '
        values += ' , %s '
        query_params.append(optional_params['isDeleted'])
        info['isDeleted'] = optional_params['isDeleted']
    query += ') values ' + values + ' )'
    info['id'] = exec_insert_update_delete_query(query, query_params)
    return info


def subscribe_thread(required_params):
    exec_insert_update_delete_query('insert into Subscriptions (user , thread) values (%s , %s)',
                                    (required_params['user'], required_params['thread'],))
    return {
        'thread': required_params['thread'],
        'user': required_params['user']
    }


def unsubscribe_thread(required_params):
    exec_insert_update_delete_query('delete from Subscriptions where user = %s and thread= %s',
                                    (required_params['user'], required_params['thread'],))
    return {
        'thread': required_params['thread'],
        'user': required_params['user']
    }


def thread_vote(required_params):
    if required_params['vote'] == 1:
        exec_insert_update_delete_query(
            'update Threads set likes = likes + 1 , points = points + 1 where id = %s',
            (required_params['thread'],))
    if required_params['vote'] == -1:
        exec_insert_update_delete_query(
            'update Threads set dislikes = dislikes + 1, points = points - 1 where id = %s',
            (required_params['thread'],))
    return get_thread_details(required_params['thread'], None)


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
    exec_insert_update_delete_query("update Threads set message = %s , slug = %s where id = %s",
                                    (required_params['message'], required_params['slug'], required_params['thread'],))
    return get_thread_details(required_params['thread'], None)


def thread_remove_restore(required_params, type):
    id = 0
    if type == 'remove':
        id = exec_insert_update_delete_query("update Threads set isDeleted = 1 where id = %s",
                                             (required_params['thread'],))
    if type == 'restore':
        id = exec_insert_update_delete_query("update Threads set isDeleted = 0 where id = %s",
                                             (required_params['thread'],))
    return {'thread': id}