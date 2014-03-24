from forumDB.functions.database import execInsertUpdateQuery
from forumDB.functions.user.getters import *
from forumDB.functions.user.getters import get_main_info, get_user_details

__author__ = 'maxim'


def save_user(required_params, anonymous):
    existed_user = find('user', None, required_params['email'])
    if existed_user is None:
        execInsertUpdateQuery(
            'insert into Users (email , name , username , about , isAnonymous ) values (%s , %s , %s , %s , %s)',
            [required_params['email'], required_params['name'], required_params['username'], required_params['about'], anonymous])
        return get_main_info(find('user', None, required_params['email']))
    else:
        return get_main_info(existed_user)


def save_follow(required_params):
    follower_user = find('user', None, required_params['follower'])
    followee_user = find('user', None, required_params['followee'])
    if follower_user == followee_user:
        return None
    if not follower_user is None and not followee_user is None:
        existed_follow = execSelectQuery(
            'select follower , followee from Followers where follower = %s and followee =%s', [required_params['follower'], required_params['followee']])
        if len(existed_follow) == 0:
            execInsertUpdateQuery('insert into Followers (follower , followee) values (%s , %s)',
                                  [required_params['follower'], required_params['followee']])
    else:
        return None
    return get_user_details(get_email(follower_user))


def remove_follow(required_params):
    follower_user = find('user', None, required_params['follower'])
    followee_user = find('user', None, required_params['followee'])
    if not follower_user is None and not followee_user is None:
        existed_follow = execSelectQuery(
            'select follower , followee from Followers where follower = %s and followee =%s', [required_params['follower'], required_params['followee']])
        if len(existed_follow) == 1:
            execInsertUpdateQuery('delete from Followers where follower = %s and followee = %s',
                                  [required_params['follower'], required_params['followee']])
            return get_user_details(get_email(follower_user))
    return None


def update_user(required_params):
    if find('user', None, required_params['email']) is not None:
        execInsertUpdateQuery('update Users set name = %s , about = %s where email = %s', [required_params['name'], required_params['about'], required_params['email']])
        return get_user_details(required_params['email'])
    else:
        return None



