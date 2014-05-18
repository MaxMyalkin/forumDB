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
            info['user'] = get_user_details(info['user'], 'email')
    return info


def forum_to_json(forum):
    return {
        'id': int(forum[0]),
        'name': forum[1],
        'short_name': forum[2],
        'user': forum[3]
    }


def get_list_posts(forum_shortname, optional_params):
    from forumDB.functions.post.getters import post_to_json
    forum = forum_shortname
    post_parameters = """p.date , p.dislikes , p.forum , p.id , p.isApproved , p.isDeleted , p.isEdited ,
        p.isHighlighted , p.isSpam , p.likes , p.message , p.parent , p.points , p.thread , p.user"""

    if optional_params['related'] is not None:
        if 'forum' in optional_params['related']:
            forum = get_forum_details(forum_shortname, [])

        if 'thread' in optional_params['related']:
            thread_parameters = """ t.date, t.dislikes , t.forum , t.id , t.isClosed , t.isDeleted , t.likes ,
            t.message , t.points , t.posts, t.slug , t.title , t.user"""
            query = ' select ' + post_parameters + ' , ' + thread_parameters + ' from Posts as p ' \
                    'inner join Threads as t on p.thread = t.id where p.forum = %s'
    else:
        query = ' select ' + post_parameters + ' from Posts as p where p.forum = %s'

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
        if optional_params['related'] is not None:
            if 'thread' in optional_params['related']:
                row_json['thread'] = thread_to_json(row[15:28])

            if 'user' in optional_params['related']:
                user = row_json['user']
                row_json['user'] = get_user_details(user, 'email')
        result.append(row_json)
    return result


def get_list_threads(required_params, optional_params):
    related = optional_params['related']
    value = required_params['forum']

    if related is not None and 'forum' in related:
        forum = get_forum_details(value, [])
    else:
        forum = value
    query = """select date, dislikes , forum , id , isClosed , isDeleted , likes , message ,points , posts, slug ,
            title, user from Threads where forum = %s """
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
            row_json['user'] = get_user_details(user, 'email')
        result.append(row_json)
    return result