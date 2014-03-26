from forumDB.functions.common import find
from forumDB.functions.database import execSelectQuery
from forumDB.functions.forum.getters import get_forum_details
from forumDB.functions.thread.getters import get_thread_details
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def get_post_details(post, related):
    if not post is None:
        info = {

        }
        if related is not None:
            for element in related:
                if element == 'user':
                    info['user'] = get_user_details(get_user(post))
                if element == 'forum':
                    info['forum'] = get_forum_details(get_forum(post), [])
                if element == 'thread':
                    info['thread'] = get_thread_details(get_thread(post),[])
        return info
    else:
        return None


def get_post_main(post):
    if not post is None:
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
        return None


def get_post_details(post, related):
    if not post is None:
        info = get_post_main(post)
        info['dislikes'] = get_dislikes(post)
        info['likes'] = get_likes(post)
        info['parent'] = get_parent(post)
        info['points'] = get_points(post)
        for parameter in related:
            if parameter == 'user':
                info['user'] = get_user_details(get_user(post))
            if parameter == 'thread':
                info['thread'] = get_thread_details(find('thread','id', get_thread(post)), [])
            if parameter == 'forum':
                info['forum'] = get_forum_details(get_forum(post), [])
        return info
    else:
        return None


def get_post_list(required_params , optional_params):
    query_params = []
    query = ''
    type = required_params['type']
    if type == 'thread':
        query = 'select id from Posts where thread = %s '
        query_params = [required_params['thread']]

    if type == 'forum':
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
    for element in execSelectQuery(query,query_params):
        list.append(get_post_details(find('post', None, element[0]), []))

    return list


def get_user_post_list(required_params , optional_params):
    query = 'select id from Posts where user = %s '
    query_params = [required_params['user']]

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
    for element in execSelectQuery(query,query_params):
        list.append(get_post_details(find('post', None, element[0]), []))

    return list



def get_forum_post_list(required_params , optional_params):
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
    for element in execSelectQuery(query,query_params):
        list.append(get_post_details(find('post', None, element[0]), optional_params['related']))

    return list


def get_thread_post_list(required_params , optional_params):
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
    for element in execSelectQuery(query,query_params):
        list.append(get_post_details(find('post', None, element[0]), []))

    return list



def get_date(post):
    if post is not None:
        return str(post[0])
    return None


def get_forum(post):
    if post is not None:
        return post[2]
    return None


def get_id(post):
    if post is not None:
        return int(post[3])
    return None


def get_dislikes(post):
    if post is not None:
        return int(post[1])
    return None


def get_approved(post):
    if post is not None:
        return bool(post[4])
    return None


def get_deleted(post):
    if post is not None:
        return bool(post[5])
    return None


def get_edited(post):
    if post is not None:
        return bool(post[6])
    return None


def get_highlighted(post):
    if post is not None:
        return bool(post[7])
    return None


def get_spam(post):
    if post is not None:
        return bool(post[8])
    return None


def get_likes(post):
    if post is not None:
        return int(post[9])
    return None


def get_message(post):
    if post is not None:
        return post[10]
    return None


def get_parent(post):
    if post is not None:
        return post[11]
    return None


def get_points(post):
    if post is not None:
        return int(post[12])
    return None


def get_thread(post):
    if post is not None:
        return int(post[13])
    return None


def get_user(post):
    if post is not None:
        return post[14]
    return None
