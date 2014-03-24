from forumDB.functions.database import execInsertUpdateQuery
from forumDB.functions.user.getters import *
from forumDB.functions.user.getters import get_main_info, get_user_details

__author__ = 'maxim'


def save_user(email, name, username, about, anonymous):
    existed_user = find('user', None, email)
    if existed_user is None:
        execInsertUpdateQuery(
            'insert into Users (email , name , username , about , isAnonymous ) values (%s , %s , %s , %s , %s)',
            [email, name, username, about, anonymous])
        return get_main_info(find('user', None, email))
    else:
        return get_main_info(existed_user)


def save_follow(follower, followee):
    follower_user = find('user', None, follower)
    followee_user = find('user', None, followee)
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
    follower_user = find('user', None, follower)
    followee_user = find('user', None, followee)
    if not follower_user is None and not followee_user is None:
        existed_follow = execSelectQuery(
            'select follower , followee from Followers where follower = %s and followee =%s', [follower, followee])
        if len(existed_follow) == 1:
            execInsertUpdateQuery('delete from Followers where follower = %s and followee = %s',
                                  [follower, followee])
            return get_user_details(follower_user[1])  # email
    return None








def update_user(email, name, about):
    if find('user', None, email) is not None:
        execInsertUpdateQuery('update Users set name = %s , about = %s where email = %s', [name, about, email])
        return get_user_details(email)
    else:
        return None



