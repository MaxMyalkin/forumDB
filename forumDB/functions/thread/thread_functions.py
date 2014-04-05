from forumDB.functions.common import find
from forumDB.functions.database import execSelectQuery, execInsertUpdateQuery
from forumDB.functions.thread.getters import get_main_info, get_thread_details, get_id

__author__ = 'maxim'


def create_thread(required_params, optional_params):
    find('user', None, required_params['user'])
    find('forum', None, required_params['forum'])
    query = 'insert into Threads (forum , title , isClosed , user , date , message , slug '
    values = '(%s, %s, %s, %s, %s, %s, %s '
    query_params = [required_params['forum'], required_params['title'], required_params['isClosed'],
                    required_params['user'], required_params['date'], required_params['message'],
                    required_params['slug']]
    if optional_params['isDeleted'] is not None:
        query += ' , isDeleted '
        values += ' , %s '
        query_params.append(optional_params['isDeleted'])
    query += ') values ' + values + ' )'
    try:
        thread = find('thread', 'slug', required_params['slug'])
    except Exception:
        execInsertUpdateQuery(query, query_params)
        thread = find('thread', 'slug', required_params['slug'])
    return get_main_info(thread)


def subscribe_thread(required_params):
    find('user', None, required_params['user'])
    find('thread', 'id', required_params['thread'])
    try:
        find_subscription(required_params['user'], required_params['thread'])
    except Exception:
        execInsertUpdateQuery('insert into Subscriptions (user , thread) values (%s , %s)',
                              (required_params['user'], required_params['thread'],))
    return subscription_info(find_subscription(required_params['user'], required_params['thread']))


def unsubscribe_thread(required_params):
    find('user', None, required_params['user'])
    find('thread', 'id', required_params['thread'])
    subscription = find_subscription(required_params['user'], required_params['thread'])
    execInsertUpdateQuery('delete from Subscriptions where user = %s and thread= %s',
                          (required_params['user'], required_params['thread'],))
    return subscription_info(subscription)


def find_subscription(user, thread_id):
    subscription = execSelectQuery('select user, thread from Subscriptions where user= %s and thread = %s',
                                   (user, thread_id,))
    if len(subscription) == 0:
        raise Exception('subscription doesnt exist')
    return subscription[0]


def subscription_info(subscription):
    if subscription is None:
        raise Exception('you cant get info of None')
    return {
        'user': subscription[0],
        'thread': subscription[1]
    }


def thread_vote(required_params):
    if required_params['vote'] == 1:
        execInsertUpdateQuery(
            'update Threads set likes = likes + 1 , points = likes - dislikes where id = %s',
            (required_params['thread'],))
    if required_params['vote'] == -1:
        execInsertUpdateQuery(
            'update Threads set dislikes = dislikes + 1, points = likes - dislikes where id = %s',
            (required_params['thread'],))
    return get_thread_details(find('thread', 'id', required_params['thread']), None)


def close_or_open(type, thread):
    if type == 'open':
        execInsertUpdateQuery('update Threads set isClosed = 0 where id = %s', (thread,))
    if type == 'close':
        execInsertUpdateQuery('update Threads set isClosed = 1 where id = %s', (thread,))
    return get_thread_details(find('thread', 'id', thread), None)


def thread_update(required_params):
    execInsertUpdateQuery("update Threads set message = %s , slug = %s where id = %s",
                          (required_params['message'], required_params['slug'], required_params['thread'],))
    return get_thread_details(find('thread', 'id', required_params['thread'],), None)


def thread_remove_restore(required_params, type):
    if type == 'remove':
        execInsertUpdateQuery("update Threads set isDeleted = 1 where id = %s", (required_params['thread'],))
    if type == 'restore':
        execInsertUpdateQuery("update Threads set isDeleted = 0 where id = %s", (required_params['thread'],))
    return {'thread': get_id(find('thread', 'id', required_params['thread']))}