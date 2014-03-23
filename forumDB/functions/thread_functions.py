from forumDB.functions.database import execSelectQuery, execInsertUpdateQuery
from forumDB.functions.forum_functions import find_forum
from forumDB.functions.user_functions import find_user

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
        'select date , forum , id , isClosed , isDeleted , message , slug , title , user  from Threads where ' + type + ' = ' + str(value),
        [])
    if len(thread) == 0:
        return None
    else:
        return thread[0]


def get_main_info(thread):
    if not thread is None:
        return {
            'date': str(thread[0]),
            'forum': thread[1],
            'id': thread[2],
            'isClosed': bool(thread[3]),
            'isDeleted': bool(thread[4]),
            'message': thread[5],
            'slug': thread[6],
            'title': thread[7],
            'user': thread[8]
        }
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
