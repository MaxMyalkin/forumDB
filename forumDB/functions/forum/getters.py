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
    if related == ['user']:
        info['user'] = get_user_details(get_user(forum))
    return info


def get_listThreads(what, value, related, optional_parameters):
    from forumDB.functions.thread.thread_functions import get_thread_details
    if (what == 'forum' and find('forum', None, value) is None) or \
            (what == 'user' and find('user', None, value) is None):
        return None
    list = []
    user = None
    forum = None
    for el in related:
        if el == 'user':
            user = 'ok'
        if el == 'forum':
            forum = 'ok'
    if optional_parameters['limit'] is None:
        for element in execSelectQuery(
                                        'select slug from Threads where ' + what + ' = %s and date >= %s order by date ' +
                        optional_parameters['order'], [value, optional_parameters['since']]):
            list.append(get_thread_details(find('thread', 'slug', element[0]), user, forum))
    else:
        for element in execSelectQuery(
                                'select slug from Threads where ' + what + '  = %s and date >=%s order by date ' +
                                optional_parameters['order'] + ' limit %s',
                                                [value, optional_parameters['since'], optional_parameters['limit']]):
            list.append(get_thread_details(find('thread', 'slug', element[0]), user, forum))
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