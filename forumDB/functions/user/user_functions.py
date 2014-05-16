from forumDB.functions.database import exec_insert_update_delete_query
from forumDB.functions.user.getters import *
from forumDB.functions.user.getters import get_main_info, get_user_details

__author__ = 'maxim'


def create_user(required_params, optional_params):
    #try:
    #    existed_user = find('user', None, required_params['email'])
    #except Exception:
     #   existed_user = None
    #if existed_user is None:
        query = 'insert into Users (email'
        values = '(%s '
        query_parameters = [required_params['email']]

        if optional_params['about'] is not None:
            query += ' , about'
            values += ' , %s'
            query_parameters.append(optional_params['about'])

        if optional_params['username'] is not None:
            query += ' , username'
            values += ' , %s'
            query_parameters.append(optional_params['username'])

        if optional_params['name'] is not None:
            query += ' , name'
            values += ' , %s'
            query_parameters.append(optional_params['name'])

        if optional_params['isAnonymous'] is not None:
            query += ' , isAnonymous'
            values += ' , %s'
            query_parameters.append(int(optional_params['isAnonymous']))
        query += ') values ' + values + ')'
        exec_insert_update_delete_query( query , query_parameters )
        return get_main_info(find('user', None, required_params['email']))
    #else:
      #  return get_main_info(existed_user)


def save_follow(required_params):
    follower_user = find('user', None, required_params['follower'])
   # followee_user = find('user', None, required_params['followee'])
    #if follower_user == followee_user:
      #  raise Exception('you cant follow to self')
    #existed_follow = exec_select_query('select follower , followee from Followers where follower = %s and followee =%s',
     #                                (required_params['follower'], required_params['followee'],))
    #if len(existed_follow) == 0:
    exec_insert_update_delete_query('insert into Followers (follower , followee) values (%s , %s)',
                              (required_params['follower'], required_params['followee'],))
    return get_user_details(get_email(follower_user))


def remove_follow(required_params):
    follower_user = find('user', None, required_params['follower'])
    #find('user', None, required_params['followee'])
   # existed_follow = exec_select_query(
     #   'select follower , followee from Followers where follower = %s and followee =%s', (required_params['follower'], required_params['followee'],))
    #if len(existed_follow) != 0:
    exec_insert_update_delete_query('delete from Followers where follower = %s and followee = %s',
                          (required_params['follower'], required_params['followee'],))
    return get_user_details(get_email(follower_user))
    #raise Exception("follow doesnt exist")


def update_user(required_params):
    #find('user', None, required_params['user'])
    exec_insert_update_delete_query('update Users set name = %s , about = %s where email = %s', (required_params['name'], required_params['about'], required_params['user'],))
    return get_user_details(required_params['user'])
