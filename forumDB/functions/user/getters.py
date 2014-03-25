from forumDB.functions.common import find
from forumDB.functions.database import execSelectQuery


__author__ = 'maxim'


def get_user_details(email):
    user = find('user', None, email)
    if user is None:
        return None
    info = get_main_info(user)
    info['followers'] = get_follows('follower', email)
    info['following'] = get_follows('followee', email)
    info['subscriptions'] = get_list_subscriptions(email)
    return info


def get_list_followers(required_params, optional_parameters):
    user = find('user', None, required_params['user'])
    if user is None:
        return None
    info = []
    for follower in get_follows_parametrized('follower', required_params['user'], optional_parameters['since'],
                                             optional_parameters['limit'], optional_parameters['order']):
        info.append(get_user_details(follower))
    return info


def get_list_following(required_params, optional_parameters):
    user = find('user', None, required_params['user'])
    if user is None:
        return None
    info = []
    for follower in get_follows_parametrized('followee', required_params['user'], optional_parameters['since'],
                                             optional_parameters['limit'], optional_parameters['order']):
        info.append(get_user_details(follower))
    return info


def get_follows(what, email):   # get following or followers
    list = []
    if what == 'followee':
        select = 'followee'
        where = 'follower'
    else:
        select = 'follower'
        where = 'followee'
    for element in execSelectQuery('select ' + select + ' from Followers where ' + where + ' = %s', [email]):
        list.append(element[0])
    return list


def get_follows_parametrized(what, email, since, limit, order):   # get following or followers
    list = []
    if what == 'followee':
        where = 'follower'
        select = 'followee'
    else:
        where = 'followee'
        select = 'follower'

    if limit is None:
        for element in execSelectQuery('select ' + select + ' from Followers as f inner join Users as u '
                                                            'on f.' + select + ' = u.email where ' + where + ' = %s and u.id >= ' + str(
                since) +
                                               ' order by u.name ' + order, [email]):
            list.append(element[0])
    else:
        for element in execSelectQuery('select ' + select + ' from Followers as f inner join Users as u '
                                                            'on f.' + select + ' = u.email where ' + where + ' = %s and u.id >= ' + str(
                since) +
                                               ' order by u.name ' + order + ' limit ' + str(limit), [email]):
            list.append(element[0])
    return list


def get_main_info(user):
    if not user is None:
        return {
            'about': get_about(user),
            'email': get_email(user),
            'id': get_id(user),
            'isAnonymous': get_isAnonymous(user),
            'name': get_name(user),
            'username': get_username(user)
        }
    else:
        return None


def get_list_subscriptions(email):
    list = []
    for element in execSelectQuery('select thread from Subscriptions where  user = %s', [email]):
        list.append(element[0])
    return list


def get_id(user):
    if user is not None:
        return user[2]
    return None


def get_email(user):
    if user is not None:
        return user[1]
    return None


def get_about(user):
    if user is not None:
        return user[0]
    return None


def get_isAnonymous(user):
    if user is not None:
        return bool(user[3])
    return None


def get_name(user):
    if user is not None:
        return user[4]
    return None


def get_username(user):
    if user is not None:
        return user[5]
    return None