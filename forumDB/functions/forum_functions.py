from forumDB.functions.thread_functions import *
from forumDB.functions.user_functions import *

__author__ = 'maxim'


def save_forum(name, short_name, user):
    creator = get_user_details(user)
    if creator is None:
        return None
    existed_forum = find_forum(short_name)
    if existed_forum is None:
        execInsertUpdateQuery('insert into Forums (name , short_name , user ) values (%s , %s , %s)',
                              [name, short_name, user])
    return get_forum_details(short_name, [])



def find_forum(short_name):
    forum = execSelectQuery('select id, name , short_name , user  from Forums where short_name = %s',
                           [short_name])
    if len(forum) == 0:
        return None
    else:
        return forum[0]


def get_forum_details(short_name , related):
    forum = find_forum(short_name)
    if forum is None:
        return None
    info = {
        'id': forum[0],
        'name': forum[1],
        'short_name': forum[2],
        'user': forum[3]
        }
    if related == ['user']:
        info['user'] = get_user_details(forum[3])
    return info


def get_listThreads(short_name , since , related , limit , order):
    list = []
    user = None
    forum = None
    for el in related:
        if el == 'user':
            user = 'ok'
        if el == 'forum':
            forum = 'ok'
    if limit is None:
            for element in execSelectQuery('select slug from Threads where forum = %s ',[short_name]):
                list.append(get_thread_details(find_thread('slug' , element[0]),user , forum))
    else:
       for element in execSelectQuery('select slug from Threads where forum = %s limit ' + str(limit),[short_name]):
                list.append(get_thread_details(find_thread('slug' , element[0]),user , forum))
    return list