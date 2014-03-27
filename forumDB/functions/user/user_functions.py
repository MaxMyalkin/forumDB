from forumDB.functions.database import execInsertUpdateQuery
from forumDB.functions.user.getters import *
from forumDB.functions.user.getters import get_main_info, get_user_details

__author__ = 'maxim'


def create_user(required_params, optional_params):
    try:
        existed_user = find('user', None, required_params['email'])
    except Exception:
        existed_user = None
    if existed_user is None:
        query = 'insert into Users (email , name , username , about'
        values = '(%s , %s , %s , %s'
        query_parameters = [required_params['email'], required_params['name'], required_params['username'], required_params['about']]
        if optional_params['isAnonymous'] is not None:
            query += ' , isAnonymous'
            values += ' , %s'
            query_parameters.append(int(optional_params['isAnonymous']))
        query += ') values ' + values + ')'
        execInsertUpdateQuery( query , query_parameters )
        return get_main_info(find('user', None, required_params['email']))
    else:
        return get_main_info(existed_user)


def save_follow(required_params):
    follower_user = find('user', None, required_params['follower'])
    followee_user = find('user', None, required_params['followee'])
    if follower_user == followee_user:
        raise Exception('you cant follow to self')
    existed_follow = execSelectQuery('select follower , followee from Followers where follower = %s and followee =%s',
                                     [required_params['follower'], required_params['followee']])
    if len(existed_follow) == 0:
        execInsertUpdateQuery('insert into Followers (follower , followee) values (%s , %s)',
                              [required_params['follower'], required_params['followee']])
    return get_user_details(get_email(follower_user))


def remove_follow(required_params):
    follower_user = find('user', None, required_params['follower'])
    find('user', None, required_params['followee'])
    existed_follow = execSelectQuery(
        'select follower , followee from Followers where follower = %s and followee =%s', [required_params['follower'], required_params['followee']])
    if len(existed_follow) != 0:
        execInsertUpdateQuery('delete from Followers where follower = %s and followee = %s',
                              [required_params['follower'], required_params['followee']])
        return get_user_details(get_email(follower_user))
    return None


def update_user(required_params):
    find('user', None, required_params['user'])
    execInsertUpdateQuery('update Users set name = %s , about = %s where email = %s', [required_params['name'], required_params['about'], required_params['user']])
    return get_user_details(required_params['user'])


