from forumDB.functions.common import find
from forumDB.functions.database import exec_select_query
from forumDB.functions.thread.getters import thread_to_json
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def get_forum_details(short_name, related):
    forum = find('forum', short_name)
    info = forum_to_json(forum)
    if related is not None:
        if 'user' in related:
            info['user'] = get_user_details(get_user(forum))
    return info


def forum_to_json(forum):
    return {
        'id': get_id(forum),
        'name': get_name(forum),
        'short_name': get_short_name(forum),
        'user': get_user(forum)
    }


def get_list_posts(forum_shortname, optional_params):
    from forumDB.functions.post.getters import post_to_json

    if optional_params['related'] is not None and 'forum' in optional_params['related']:
        forum = get_forum_details(forum_shortname, [])
    else:
        forum = forum_shortname
    forum_parameters = """p.date , p.dislikes , p.forum , p.id , p.isApproved , p.isDeleted , p.isEdited ,
        p.isHighlighted , p.isSpam , p.likes , p.message , p.parent , p.points , p.thread , p.user"""

    thread_parameters = """ t.date, t.dislikes , t.forum , t.id , t.isClosed , t.isDeleted , t.likes , t.message ,
    t.points , t.posts, t.slug , t.title , t.user"""

    query = ' select ' + forum_parameters + ' , ' + thread_parameters + ' from Posts as p inner join Threads as t on p.thread = t.id where p.forum = %s'
    query_params = [forum_shortname]
    if optional_params['since'] is not None:
        query += ' and p.date >= %s '
        query_params.append(optional_params['since'])

    if optional_params['order'] is not None:
        query += ' order by p.date ' + optional_params['order']
    else:
        query += ' order by p.date desc '

    if optional_params['limit'] is not None:
        query += ' limit ' + str(optional_params['limit'])

    list = exec_select_query(query, query_params)
    result = []

    for row in list:
        row_json = post_to_json(row[0:15])

        row_json['forum'] = forum
        if optional_params['related'] is not None and 'thread' in optional_params['related']:
            row_json['thread'] = thread_to_json(row[15:28])

        if optional_params['related'] is not None and 'user' in optional_params['related']:
            user = row_json['user']
            row_json['user'] = get_user_details(user)
        result.append(row_json)
    return result


def get_list_threads(what, value, related, optional_params):

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
    result = []
    for row in list:
        row_json = thread_to_json(row)
        row_json['forum'] = forum
        if related is not None and 'user' in related:
            user = row_json['user']
            row_json['user'] = get_user_details(user)
        result.append(row_json)
    return result


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