from forumDB.functions.common import find
from forumDB.functions.database import exec_select_query
from forumDB.functions.forum.getters import get_forum_details
from forumDB.functions.thread.getters import get_thread_details
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def get_post_main(post):
    if post is not None:
        info = {
            'date': get_date(post),
            'forum': get_forum(post),
            'id': get_id(post),
            'isApproved': get_approved(post),
            'isDeleted': get_deleted(post),
            'isEdited': get_edited(post),
            'isHighlighted': get_highlighted(post),
            'isSpam': get_spam(post),
            'message': get_message(post),
            'thread': get_thread(post),
            'user': get_user(post)
        }
        return info
    else:
        raise Exception('you cant get info of None')


def get_post_details(post, related):
    if post is not None:
        info = get_post_main(post)
        info['dislikes'] = get_dislikes(post)
        info['likes'] = get_likes(post)
        parent = get_parent(post)
        if parent == 'null':
            info['parent'] = None
        else:
            info['parent'] = parent
        info['points'] = get_points(post)
        if related is not None:
            if 'user' in related:
                info['user'] = get_user_details(get_user(post))
            if 'thread' in related:
                info['thread'] = get_thread_details(find('thread', 'id', get_thread(post)), [])
            if 'forum' in related:
                info['forum'] = get_forum_details(get_forum(post), [])
        return info
    else:
        raise Exception('you cant get info of None')


def get_post_list(required_params, optional_params):
    query_params = []
    type = required_params['type']
    query = """select date , dislikes , forum , id , isApproved , isDeleted , isEdited ,
    isHighlighted , isSpam , likes , message , parent , points , thread , user from Posts where """ \
            + type + " = %s"
    query_params.append(required_params[type])

    if optional_params['since'] is not None:
        query += ' and date >= %s '
        query_params.append(optional_params['since'])

    if optional_params['order'] is not None:
        query += ' order by date ' + optional_params['order']
    else:
        query += ' order by date desc '

    if optional_params['limit'] is not None:
        query += ' limit ' + optional_params['limit']

    list = exec_select_query(query, query_params)
    array = []
    for row in list :
        array.append(get_post_details(row, []))
    return array


def get_user_post_list(required_params, optional_params):
    #find('user', None, required_params['user'])
    query = 'select  from Posts where user = %s '
    query_params = [required_params['user']]

    if optional_params['since'] is not None:
        query += ' and date >= %s '
        query_params.append(optional_params['since'])

    if optional_params['order'] is not None:
        query += ' order by date ' + optional_params['order']
    else:
        query += ' order by date desc '

    if optional_params['limit'] is not None:
        query += ' limit ' + optional_params['limit']

    list = []
    for element in exec_select_query(query, query_params):
        list.append(get_post_details(find('post', None, element[0]), []))
    return list


def get_forum_post_list(required_params, optional_params):
    #find('forum', None, required_params['forum'])
    query = 'select id from Posts where forum = %s '
    query_params = [required_params['forum']]

    if optional_params['since'] is not None:
        query += ' and date >= %s '
        query_params.append(optional_params['since'])

    if optional_params['order'] is not None:
        query += ' order by date ' + optional_params['order']
    else:
        query += ' order by desc '

    if optional_params['limit'] is not None:
        query += ' limit ' + optional_params['limit']

    list = []
    for element in exec_select_query(query, query_params):
        list.append(get_post_details(find('post', None, element[0]), optional_params['related']))
    return list


def get_thread_user_post_list(type, required_params, optional_params):
    #find('thread', 'id', required_params['thread'])
    query = 'select id from Posts where thread = %s '
    query_params = [required_params['thread']]

    if optional_params['since'] is not None:
        query += ' and date >= %s '
        query_params.append(optional_params['since'])

    if optional_params['order'] is not None:
        query += ' order by date ' + optional_params['order']
    else:
        query += ' order by desc '

    if optional_params['limit'] is not None:
        query += ' limit ' + optional_params['limit']

    list = []
    for element in exec_select_query(query, query_params):
        list.append(get_post_details(find('post', None, element[0]), []))
    return list


def get_date(post):
    if post is not None:
        return str(post[0])
    raise Exception('you cant get info of None')


def get_forum(post):
    if post is not None:
        return post[2]
    raise Exception('you cant get info of None')


def get_id(post):
    if post is not None:
        return int(post[3])
    raise Exception('you cant get info of None')


def get_dislikes(post):
    if post is not None:
        return int(post[1])
    raise Exception('you cant get info of None')


def get_approved(post):
    if post is not None:
        return bool(post[4])
    raise Exception('you cant get info of None')


def get_deleted(post):
    if post is not None:
        return bool(post[5])
    raise Exception('you cant get info of None')


def get_edited(post):
    if post is not None:
        return bool(post[6])
    raise Exception('you cant get info of None')


def get_highlighted(post):
    if post is not None:
        return bool(post[7])
    raise Exception('you cant get info of None')


def get_spam(post):
    if post is not None:
        return bool(post[8])
    raise Exception('you cant get info of None')


def get_likes(post):
    if post is not None:
        return int(post[9])
    raise Exception('you cant get info of None')


def get_message(post):
    if post is not None:
        return post[10]
    raise Exception('you cant get info of None')


def get_parent(post):
    if post is not None:
        return post[11]
    raise Exception('you cant get info of None')


def get_points(post):
    if post is not None:
        return int(post[12])
    raise Exception('you cant get info of None')


def get_thread(post):
    if post is not None:
        return int(post[13])
    raise Exception('you cant get info of None')


def get_user(post):
    if post is not None:
        return post[14]
    raise Exception('you cant get info of None')
