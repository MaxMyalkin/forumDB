from forumDB.functions.common import find
from forumDB.functions.database import exec_select_query
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def get_forum_details(short_name, related):
    forum = find('forum', None, short_name)
    info = {
        'id': get_id(forum),
        'name': get_name(forum),
        'short_name': get_short_name(forum),
        'user': get_user(forum)
    }
    if related is not None:
        if 'user' in related:
            info['user'] = get_user_details(get_user(forum))
    return info


def get_list_threads(what, value, related, optional_params):
    from forumDB.functions.thread.getters import get_thread_info
    if related is not None and 'forum' in related:
        forum = get_forum_details(value, [])
    else:
        forum = value
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
        row_json = get_thread_info(row)
        row_json['forum'] = forum
        if 'user' in forum:
            user = row_json['user']
            row_json['user'] = get_user_details(user)
        array.append(row_json)
    return array


def get_id(forum):
    if forum is not None:
        return int(forum[0])
    raise Exception('you cant get info of None')


def get_name(forum):
    if forum is not None:
        return forum[1]
    raise Exception('you cant get info of None')


def get_short_name(forum):
    if forum is not None:
        return forum[2]
    raise Exception('you cant get info of None')


def get_user(forum):
    if forum is not None:
        return forum[3]
    raise Exception('you cant get info of None')