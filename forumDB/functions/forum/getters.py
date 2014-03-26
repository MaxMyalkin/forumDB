from forumDB.functions.common import find
from forumDB.functions.database import execSelectQuery
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def get_forum_details(short_name, related):
    forum = find('forum', None, short_name)
    if forum is None:
        return None
    info = {
        'id': get_id(forum),
        'name': get_name(forum),
        'short_name': get_short_name(forum),
        'user': get_user(forum)
    }
    if related == 'user':
        info['user'] = get_user_details(get_user(forum))
    return info


def get_listThreads(what, value, related, optional_params):
    from forumDB.functions.thread.thread_functions import get_thread_details
    if (what == 'forum' and find('forum', None, value) is None) or \
            (what == 'user' and find('user', None, value) is None):
        return None
    list = []

    query = 'select slug from Threads where ' + what + ' = %s '
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

    for element in execSelectQuery(query , query_params):
            list.append(get_thread_details(find('thread', 'slug', element[0]), related))
    return list


def get_id(forum):
    if forum is not None:
        return int(forum[0])
    return None


def get_name(forum):
    if forum is not None:
        return forum[1]
    return None


def get_short_name(forum):
    if forum is not None:
        return forum[2]
    return None


def get_user(forum):
    if forum is not None:
        return forum[3]
    return None