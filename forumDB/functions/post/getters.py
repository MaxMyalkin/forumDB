from forumDB.functions.common import find
from forumDB.functions.database import exec_select_query
from forumDB.functions.forum.getters import forum_to_json

from forumDB.functions.thread.getters import thread_to_json
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def get_post_main(post):
    post = find('post', post)
    return post_to_json(post)


def post_to_json(post):
    parent = post[11]
    if parent == 'null':
        parent = None
    return {
        'date': str(post[0]),
        'dislikes': int(post[1]),
        'forum': post[2],
        'id': int(post[3]),
        'isApproved': bool(post[4]),
        'isDeleted': bool(post[5]),
        'isEdited': bool(post[6]),
        'isHighlighted': bool(post[7]),
        'isSpam': bool(post[8]),
        'likes': int(post[9]),
        'message': post[10],
        'parent': parent,
        'points': int(post[12]),
        'thread': int(post[13]),
        'user': post[14]
    }


def get_post_details(post, related):
    thread_parameters = """ t.date, t.dislikes, t.forum, t.id, t.isClosed, t.isDeleted, t.likes, t.message, t.points,
                      t.posts, t.slug, t.title, t.user """

    post_parameters = """ p.date, p.dislikes, p.forum, p.id, p.isApproved, p.isDeleted, p.isEdited,
                                 p.isHighlighted, p.isSpam, p.likes, p.message, p.parent, p.points, p.thread, p.user """

    forum_parameters = """ f.id, f.name, f.short_name, f.user """

    columns = "select " + post_parameters
    tables = " from Posts p "
    forum_in_related = False
    if related is not None:
        if 'forum' in related:
            columns += ", " + forum_parameters
            tables += "join Forums f on p.forum = f.short_name "
            forum_in_related = True
        if 'thread' in related:
            columns += ", " + thread_parameters
            tables += " join Threads t on p.thread = t.id "

    query = columns + tables + " where p.id = %s"

    result = exec_select_query(query, (int(post),))

    info = post_to_json(result[0][0:15])
    if related is not None:
        if 'user' in related:
            info['user'] = get_user_details(info['user'], 'email')
        if 'forum' in related:
            info['forum'] = forum_to_json(result[0][15:19])
        if 'thread' in related:
            if forum_in_related:
                info['thread'] = thread_to_json(result[0][19:32])
            else:
                info['thread'] = thread_to_json(result[0][15:28])

    return info


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
    for row in list:
        array.append(post_to_json(row))
    return array


#def get_user_post_list(required_params, optional_params):
#    #find('user', None, required_params['user'])
#    query = 'select  from Posts where user = %s '
#    query_params = [required_params['user']]
#
#    if optional_params['since'] is not None:
#        query += ' and date >= %s '
#        query_params.append(optional_params['since'])
#
#    if optional_params['order'] is not None:
#        query += ' order by date ' + optional_params['order']
#    else:
#        query += ' order by date desc '
#
#    if optional_params['limit'] is not None:
#        query += ' limit ' + optional_params['limit']
#
#    list = []
#    for element in exec_select_query(query, query_params):
#        list.append(get_post_details(find('post', None, element[0]), []))
#    return list
#
#
#def get_forum_post_list(required_params, optional_params):
#    #find('forum', None, required_params['forum'])
#    query = 'select id from Posts where forum = %s '
#    query_params = [required_params['forum']]
#
#    if optional_params['since'] is not None:
#        query += ' and date >= %s '
#        query_params.append(optional_params['since'])
#
#    if optional_params['order'] is not None:
#        query += ' order by date ' + optional_params['order']
#    else:
#        query += ' order by desc '
#
#    if optional_params['limit'] is not None:
#        query += ' limit ' + optional_params['limit']
#
#    list = []
#    for element in exec_select_query(query, query_params):
#        list.append(get_post_details(find('post', None, element[0]), optional_params['related']))
#    return list
#
#
#def get_thread_user_post_list(type, required_params, optional_params):
#    #find('thread', 'id', required_params['thread'])
#    query = 'select id from Posts where thread = %s '
#    query_params = [required_params['thread']]
#
#    if optional_params['since'] is not None:
#        query += ' and date >= %s '
#        query_params.append(optional_params['since'])
#
#    if optional_params['order'] is not None:
#        query += ' order by date ' + optional_params['order']
#    else:
#        query += ' order by desc '
#
#    if optional_params['limit'] is not None:
#        query += ' limit ' + optional_params['limit']
#
#    list = []
#    for element in exec_select_query(query, query_params):
#        list.append(get_post_details(find('post', None, element[0]), []))
#    return list
