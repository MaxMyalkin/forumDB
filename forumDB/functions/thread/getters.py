from forumDB.functions.database import exec_select_query
from forumDB.functions.forum.forum_functions import get_forum_details
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def get_list(what, value, optional_params):

    query = """select date, dislikes , forum , id , isClosed , isDeleted , likes , message ,points , posts, slug , title ,
            user from Threads where """ + what + """ = %s """
    query_params = [value]

    if optional_params['since'] is not None:
        query += ' and date >= %s '
        query_params.append(optional_params['since'])

    if optional_params['order'] is not None:
        query += ' order by date ' + optional_params['order']
    else:
        query += ' order by date desc '

    if optional_params['limit'] is not None:
        query += ' limit ' + str(optional_params['limit'])

    list = exec_select_query(query, query_params)
    array = []
    for row in list:
        array.append(get_thread_info(row))
    return array


def get_thread_info(thread):
    return {
        'date': get_date(thread),
        'forum': get_forum(thread),
        'id': get_id(thread),
        'isClosed': get_isClosed(thread),
        'isDeleted': get_isDeleted(thread),
        'message': get_message(thread),
        'slug': get_slug(thread),
        'title': get_title(thread),
        'user': get_user(thread),
        'posts': get_posts(thread),
    }


def get_thread_details(thread, related):
    info = {
        'date': get_date(thread),
        'dislikes': get_dislikes(thread),
        'forum': get_forum(thread),
        'id': get_id(thread),
        'isClosed': get_isClosed(thread),
        'isDeleted': get_isDeleted(thread),
        'likes': get_likes(thread),
        'message': get_message(thread),
        'points': get_points(thread),
        'posts': get_posts(thread),
        'slug': get_slug(thread),
        'title': get_title(thread),
        'user': get_user(thread)
    }

    if related is not None:
        if 'user' in related:
            info['user'] = get_user_details(get_user(thread))
        if 'forum' in related:
            info['forum'] = get_forum_details(get_forum(thread), [])
    return info


def get_date(thread):
    if thread is not None:
        return str(thread[0])
    raise Exception('you cant get info of None')


def get_dislikes(thread):
    if thread is not None:
        return int(thread[1])
    raise Exception('you cant get info of None')


def get_forum(thread):
    if thread is not None:
        return thread[2]
    raise Exception('you cant get info of None')


def get_id(thread):
    if thread is not None:
        return int(thread[3])
    raise Exception('you cant get info of None')


def get_isClosed(thread):
    if thread is not None:
        return bool(thread[4])
    raise Exception('you cant get info of None')


def get_isDeleted(thread):
    if thread is not None:
        return bool(thread[5])
    raise Exception('you cant get info of None')


def get_likes(thread):
    if thread is not None:
        return int(thread[6])
    raise Exception('you cant get info of None')

def get_message(thread):
    if thread is not None:
        return thread[7]
    raise Exception('you cant get info of None')


def get_points(thread):
    if thread is not None:
        return int(thread[8])
    raise Exception('you cant get info of None')


def get_posts(thread):
    if thread is not None:
        return int(thread[9])
    raise Exception('you cant get info of None')


def get_slug(thread):
    if thread is not None:
        return thread[10]
    raise Exception('you cant get info of None')


def get_title(thread):
    if thread is not None:
        return thread[11]
    raise Exception('you cant get info of None')


def get_user(thread):
    if thread is not None:
        return thread[12]
    raise Exception('you cant get info of None')