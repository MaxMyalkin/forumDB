from forumDB.functions.common import find
from forumDB.functions.database import exec_select_query


__author__ = 'maxim'


def get_user_details(email):
    info = get_main_info(find('user', None, email))
    info['followers'] = get_follows('follower', email)
    info['following'] = get_follows('followee', email)
    info['subscriptions'] = get_list_subscriptions(email)
    return info


def get_list_followers(required_params, optional_parameters):
    find('user', None, required_params['user'])
    info = []
    for follower in get_follows_parametrized('follower', required_params, optional_parameters):
        info.append(get_user_details(follower))
    return info


def get_list_following(required_params, optional_parameters):
    find('user', None, required_params['user'])
    info = []
    for follower in get_follows_parametrized('followee', required_params, optional_parameters):
        info.append(get_user_details(follower))
    return info


def get_follows(what, email):
    list = []
    if what == 'followee':
        select = 'followee'
        where = 'follower'
    else:
        select = 'follower'
        where = 'followee'
    for element in exec_select_query('select ' + select + ' from Followers where ' + where + ' = %s', (email,)):
        list.append(element[0])
    return list


def get_follows_parametrized(what, required_params, optional_params):
    list = []
    if what == 'followee':
        where = 'follower'
        select = 'followee'
    else:
        where = 'followee'
        select = 'follower'

    query = 'select ' + select + ' from Followers as f inner join Users as u on f.' \
            + select + ' = u.email where ' + where + ' = %s'

    if optional_params['since_id'] is not None:
        query += ' and u.id >= ' + str(optional_params['since_id'])

    if optional_params['order'] is not None:
        query += ' order by u.name ' + optional_params['order']
    else:
        query += ' order by u.name desc '

    if optional_params['limit'] is not None:
        query += ' limit ' + str(optional_params['limit'])

    for element in exec_select_query(query, (required_params['user'],)):
        list.append(element[0])
    return list


def get_main_info(user):
    return {
        'about': get_about(user),
        'email': get_email(user),
        'id': get_id(user),
        'isAnonymous': get_isAnonymous(user),
        'name': get_name(user),
        'username': get_username(user)
    }


def get_list_subscriptions(email):
    list = []
    for element in exec_select_query('select thread from Subscriptions where  user = %s', (email,)):
        list.append(element[0])
    return list


def get_forum_user_list(required_params, optional_params):
    find('forum', None, required_params['forum'])
    query = 'select distinct Posts.user , Users.id as id from Posts inner join Forums on Posts.forum = Forums.short_name inner join Users ' \
            ' on Posts.user = Users.email where Forums.short_name = %s '
    query_params = [required_params['forum']]

    if optional_params['since_id'] is not None:
        query += ' and Users.id >= %s '
        query_params.append(optional_params['since_id'])

    if optional_params['order'] is not None:
        query += ' order by id ' + optional_params['order']
    else:
        query += ' order by id desc '

    if optional_params['limit'] is not None:
        query += ' limit ' + optional_params['limit']

    list = []
    for element in exec_select_query(query, query_params):
        list.append(get_user_details(element[0]))
    return list


def get_id(user):
    if user is not None:
        return user[2]
    raise Exception('you cant get info of None')


def get_email(user):
    if user is not None:
        return user[1]
    raise Exception('you cant get info of None')


def get_about(user):
    if user is not None:
        return user[0]
    raise Exception('you cant get info of None')


def get_isAnonymous(user):
    if user is not None:
        return bool(user[3])
    raise Exception('you cant get info of None')


def get_name(user):
    if user is not None:
        return user[4]
    raise Exception('you cant get info of None')


def get_username(user):
    if user is not None:
        return user[5]
    raise Exception('you cant get info of None')
