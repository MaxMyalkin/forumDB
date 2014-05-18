from forumDB.functions.database import exec_select_query
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def thread_to_json(thread):
    return {
        'date': str(thread[0]),
        'dislikes': int(thread[1]),
        'forum': thread[2],
        'id': int(thread[3]),
        'isClosed': bool(thread[4]),
        'isDeleted': bool(thread[5]),
        'likes': int(thread[6]),
        'message': thread[7],
        'points': int(thread[8]),
        'posts': int(thread[9]),
        'slug': thread[10],
        'title': thread[11],
        'user': thread[12]
    }


def get_thread_details(thread, related):
    from forumDB.functions.forum.getters import forum_to_json
    thread_parameters = ' date, dislikes , forum , Threads.id , isClosed , isDeleted , likes , message ,points , posts, slug , title ,Threads.user '
    #0-12
    if related is not None and 'forum' in related:
        forum_parameters = 'Forums.id, name , short_name , Forums.user '
    #12-16
        query = 'select ' + thread_parameters + ',' + forum_parameters + \
                "from Threads inner join Forums on Threads.forum = Forums.short_name where Threads.id = %s"
    else:
        query = "select " + thread_parameters + " from Threads where id = %s"

    result = exec_select_query(query, (thread,))

    info = thread_to_json(result[0])

    if related is not None:
        if 'user' in related:
            info['user'] = get_user_details(info['user'], 'email')
        if 'forum' in related:
            info['forum'] = forum_to_json(result[0][13:17])
    return info


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
        array.append(thread_to_json(row))
    return array