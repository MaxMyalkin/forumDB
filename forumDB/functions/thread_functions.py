from forumDB.functions.database import execSelectQuery, execInsertUpdateQuery
from forumDB.functions.forum_functions import *
from forumDB.functions.user_functions import *

__author__ = 'maxim'


def save_thread(forum, title, isClosed, user, date, message, slug, isDeleted):
    user = find_user(user)
    forum = find_forum(forum)
    if user is not None and forum is not None:
        user = user[1]
        forum = forum[2]
        thread = find_thread('slug', slug)
        if thread is None:
            execInsertUpdateQuery(
                'insert into Threads (forum , title , isClosed , user , date , message , slug , isDeleted) values (%s, %s, %s, %s, %s, %s, %s, %s)',
                [forum, title, isClosed, user, date, message, slug, isDeleted])
            thread = find_thread('slug', slug)
        return get_main_info(thread)
    return None


def find_thread(type, value):
    thread = execSelectQuery(
        'select date, dislikes , forum , id , isClosed , isDeleted , likes , message ,points , posts, slug , title , '
        'user  from Threads where ' + type + ' = %s', [value])
    if len(thread) == 0:
        return None
    else:
        return thread[0]


def get_main_info(thread):
    if not thread is None:
        return {
            'date': str(thread[0]),
            'forum': thread[2],
            'id': thread[3],
            'isClosed': bool(thread[4]),
            'isDeleted': bool(thread[5]),
            'message': thread[7],
            'slug': thread[10],
            'title': thread[11],
            'user': thread[12],

        }
    else:
        return None


def get_thread_details(thread , rel_user , rel_forum):
    if not thread is None:
        info = {
            'date': str(thread[0]),
            'dislikes': int(thread[1]),
            'forum': thread[2],
            'id': thread[3],
            'isClosed': bool(thread[4]),
            'isDeleted': bool(thread[5]),
            'likes': int(thread[6]),
            'message': thread[7],
            'points': thread[8],
            'posts': thread[9],
            'slug': thread[10],
            'title': thread[11],
            'user': thread[12]
        }
        if rel_user is not None:
            info['user'] = get_user_details(thread[12])
        if rel_forum is not None:
            info['forum'] = get_forum_details(thread[2],[])
        return info
    else:
        return None


def subscribe_thread(user, thread_id):
    subscriber = find_user(user)
    thread = find_thread('id', thread_id)
    if subscriber is not None and thread is not None:
        subscription = find_subscription(user, thread_id)
        if subscription is None:
            execInsertUpdateQuery('insert into Subscriptions (user , thread) values (%s , %s)', [user, thread_id])
            subscription = find_subscription(user, thread_id)
        return subscription_info(subscription)


def unsubscribe_thread(user, thread_id):
    subscriber = find_user(user)
    thread = find_thread('id', thread_id)
    if subscriber is not None and thread is not None:
        subscription = find_subscription(user, thread_id)
        if subscription is not None:
            execInsertUpdateQuery('delete from Subscriptions where user = %s and thread= %s', [user, thread_id])
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


def thread_vote(thread, vote):
    if vote == 1:
        execInsertUpdateQuery(
            'update Threads set likes = likes + 1 , points = likes - dislikes where id =' + str(thread), [])
    if vote == -1:
        execInsertUpdateQuery(
            'update Threads set dislikes = dislikes + 1, points = likes - dislikes where id =' + str(thread), [])
    return get_thread_details(find_thread('id', thread) , None , None)


def close_or_open(type, thread):
    if type == 'open':
        execInsertUpdateQuery('update Threads set isClosed = 0 where id = %s', [thread])
    if type == 'close':
        execInsertUpdateQuery('update Threads set isClosed = 1 where id = %s', [thread])
    return get_thread_details(find_thread('id', thread) , None)