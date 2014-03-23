from forumDB.functions.database import execSelectQuery, execInsertUpdateQuery

__author__ = 'maxim'


def save_user(email, name, username, about, anonymous):
    existed_user = find_user(email)
    if existed_user is None:
        execInsertUpdateQuery(
            'insert into Users (email , name , username , about , isAnonymous ) values (%s , %s , %s , %s , %s)',
            [email, name, username, about, anonymous])
        return get_main_info(find_user(email))
    else:
        return get_main_info(existed_user)


def find_user(email):
    user = execSelectQuery('select about , email , id , isAnonymous , name , username from Users where email = %s',
                           [email])
    if len(user) == 0:
        return None
    else:
        return user[0]


def save_follow(follower, followee):
    follower_user = find_user(follower)
    followee_user = find_user(followee)
    if follower_user == followee_user:
        return None
    if not follower_user is None and not followee_user is None:
        existed_follow = execSelectQuery(
            'select follower , followee from Followers where follower = %s and followee =%s', [follower, followee])
        if len(existed_follow) == 0:
            execInsertUpdateQuery('insert into Followers (follower , followee) values (%s , %s)',
                                  [follower, followee])
    else:
        return None
    return get_user_details(follower_user[1])


def remove_follow(follower, followee):
    follower_user = find_user(follower)
    followee_user = find_user(followee)
    if not follower_user is None and not followee_user is None:
        existed_follow = execSelectQuery(
            'select follower , followee from Followers where follower = %s and followee =%s', [follower, followee])
        if len(existed_follow) == 1:
            execInsertUpdateQuery('delete from Followers where follower = %s and followee = %s',
                                  [follower, followee])
            return get_user_details(follower_user[1])  # email
    return None


def get_user_details(email):
    user = find_user(email)
    if user is None:
        return None
    info = get_main_info(user)
    info['followers'] = get_follows('follower', email)
    info['following'] = get_follows('followee', email)
    info['subscriptions'] = get_list_subscriptions(email)
    return info


def get_list_followers(email, limit, since, order):
    user = find_user(email)
    if user is None:
        return None
    info = []
    for follower in get_follows_parametrized('follower', email, since, limit, order):
        info.append(get_user_details(follower))
    return info


def get_list_following(email, limit, since, order):
    user = find_user(email)
    if user is None:
        return None
    info = []
    for follower in get_follows_parametrized('followee', email, since, limit, order):
        info.append(get_user_details(follower))
    return info


def get_follows(what, email):   # get following or followers
    list = []
    if what == 'followee':
        select = 'followee'
        where = 'follower'
    if what == 'follower':
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
    if what == 'follower':
        where = 'followee'
        select = 'follower'

    if limit is None:
            for element in execSelectQuery('select ' + select + ' from Followers as f inner join Users as u '
                                           'on f.'+ select +' = u.email where ' + where + ' = %s and u.id >= ' + str(since) +
                                                   ' order by u.name ' + order, [email]):
                list.append(element[0])
    else:
       for element in execSelectQuery('select ' + select + ' from Followers as f inner join Users as u '
                                           'on f.'+ select +' = u.email where ' + where + ' = %s and u.id >= ' + str(since) +
                                                   ' order by u.name ' + order + ' limit ' + str(limit), [email]):
                list.append(element[0])
    return list


def update_user(email, name, about):
    if find_user(email) is not None:
        execInsertUpdateQuery('update Users set name = %s , about = %s where email = %s', [name, about, email])
        return get_user_details(email)
    else:
        return None


def get_main_info(user):
    if not user is None:
        return {
            'about': user[0],
            'email': user[1],
            'id': user[2],
            'isAnonymous': user[3],
            'name': user[4],
            'username': user[5]
        }
    else:
        return None


def get_list_subscriptions(email):
    list = []
    for element in execSelectQuery('select thread from Subscriptions where  user = %s', [email]):
        list.append(element[0])
    return list