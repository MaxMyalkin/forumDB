from forumDB.functions.common import find
from forumDB.functions.database import execSelectQuery, execInsertUpdateQuery
from forumDB.functions.thread.getters import get_main_info, get_thread_details

__author__ = 'maxim'


def save_thread(forum, title, isClosed, user, date, message, slug, isDeleted):
    user = find('user', None, user)
    forum = find('forum', None, forum)
    if user is not None and forum is not None:
        user = user[1]
        forum = forum[2]
        thread = find('thread', 'slug', slug)
        if thread is None:
            execInsertUpdateQuery(
                'insert into Threads (forum , title , isClosed , user , date , message , slug , isDeleted) values (%s, %s, %s, %s, %s, %s, %s, %s)',
                [forum, title, isClosed, user, date, message, slug, isDeleted])
            thread = find('thread', 'slug', slug)
        return get_main_info(thread)
    return None


def subscribe_thread(user, thread_id):
    subscriber = find('user', None, user)
    thread = find('thread', 'id', thread_id)
    if subscriber is not None and thread is not None:
        subscription = find_subscription(user, thread_id)
        if subscription is None:
            execInsertUpdateQuery('insert into Subscriptions (user , thread) values (%s , %s)', [user, thread_id])
            subscription = find_subscription(user, thread_id)
        return subscription_info(subscription)


def unsubscribe_thread(user, thread_id):
    subscriber = find('user', None, user)
    thread = find('thread', 'id', thread_id)
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
    return get_thread_details(find('thread', 'id', thread), None, None)


def close_or_open(type, thread):
    if type == 'open':
        execInsertUpdateQuery('update Threads set isClosed = 0 where id = %s', [thread])
    if type == 'close':
        execInsertUpdateQuery('update Threads set isClosed = 1 where id = %s', [thread])
    return get_thread_details(find('thread', 'id', thread), None, None)


def thread_update(message, slug, thread):
    threads = execSelectQuery('select slug from Threads where slug = %s' , [slug])
    if len(threads) == 0:
        execInsertUpdateQuery("update Threads set message = %s , slug = %s where id = %s" , [message, slug , thread])
        return get_thread_details(find('thread', 'id', thread), None, None)
    else:
        return None
