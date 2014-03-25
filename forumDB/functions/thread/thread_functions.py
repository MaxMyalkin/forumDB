from forumDB.functions.common import find
from forumDB.functions.database import execSelectQuery, execInsertUpdateQuery
from forumDB.functions.thread.getters import get_main_info, get_thread_details

__author__ = 'maxim'


def save_thread(required_params, isDeleted):
    user = find('user', None, required_params['user'])
    forum = find('forum', None, required_params['forum'])
    if user is not None and forum is not None:
        thread = find('thread', 'slug', required_params['slug'])
        if thread is None:
            execInsertUpdateQuery(
                'insert into Threads (forum , title , isClosed , user , date , message , slug , isDeleted) values (%s, %s, %s, %s, %s, %s, %s, %s)',
                [required_params['forum'], required_params['title'], required_params['isClosed'], required_params['user'],
                 required_params['date'], required_params['message'], required_params['slug'], isDeleted])
            thread = find('thread', 'slug', required_params['slug'])
        return get_main_info(thread)
    return None


def subscribe_thread(required_params):
    subscriber = find('user', None, required_params['user'])
    thread = find('thread', 'id', required_params['thread'])
    if subscriber is not None and thread is not None:
        subscription = find_subscription(required_params['user'], required_params['thread'])
        if subscription is None:
            execInsertUpdateQuery('insert into Subscriptions (user , thread) values (%s , %s)', [required_params['user'], required_params['thread']])
            subscription = find_subscription(required_params['user'], required_params['thread'])
        return subscription_info(subscription)


def unsubscribe_thread(required_params):
    subscriber = find('user', None, required_params['user'])
    thread = find('thread', 'id', required_params['thread'])
    if subscriber is not None and thread is not None:
        subscription = find_subscription(required_params['user'], required_params['thread'])
        if subscription is not None:
            execInsertUpdateQuery('delete from Subscriptions where user = %s and thread= %s', [required_params['user'], required_params['thread']])
            return subscription_info(subscription)
        else:
            return None


def find_subscription(user, thread_id):
    subscription = execSelectQuery('select user, thread from Subscriptions where user= %s and thread = %s',
                                   [user, thread_id])
    if len(subscription) == 0:
        return None
    return subscription[0]


def subscription_info(subscription):
    if subscription is None:
        return None
    return {
        'user': subscription[0],
        'thread': subscription[1]
    }


def thread_vote(required_params):
    if required_params['vote'] == 1:
        execInsertUpdateQuery(
            'update Threads set likes = likes + 1 , points = likes - dislikes where id = %s', [required_params['thread']])
    if required_params['vote'] == -1:
        execInsertUpdateQuery(
            'update Threads set dislikes = dislikes + 1, points = likes - dislikes where id = %s', [required_params['thread']])
    return get_thread_details(find('thread', 'id', required_params['thread']), None, None)


def close_or_open(type, thread):
    if type == 'open':
        execInsertUpdateQuery('update Threads set isClosed = 0 where id = %s', [thread])
    if type == 'close':
        execInsertUpdateQuery('update Threads set isClosed = 1 where id = %s', [thread])
    return get_thread_details(find('thread', 'id', thread), None, None)


def thread_update(required_params):
    threads = execSelectQuery('select slug from Threads where slug = %s' , [required_params['slug']])
    if len(threads) == 0:
        execInsertUpdateQuery("update Threads set message = %s , slug = %s where id = %s" , [required_params['message'], required_params['slug'] , required_params['thread']])
        return get_thread_details(find('thread', 'id', required_params['thread']), None, None)
    else:
        return None
