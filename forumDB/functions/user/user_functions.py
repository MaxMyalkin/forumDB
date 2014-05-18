from forumDB.functions.database import exec_insert_update_delete_query
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def create_user(required_params, optional_params):
    query = 'insert into Users (email, about, username, name'
    values = '(%s, %s, %s, %s '
    query_parameters = [required_params['email'], required_params['about'], required_params['username'],
                        required_params['name']]

    info = {'email': required_params['email'],
            'about': required_params['about'],
            'username': required_params['username'],
            'name': required_params['name']
            }

    if optional_params['isAnonymous'] is not None:
        query += ' , isAnonymous'
        values += ' , %s'
        info['isAnonymous'] = optional_params['isAnonymous']
        query_parameters.append(int(optional_params['isAnonymous']))
    else:
        info['isAnonymous'] = False
    query += ') values ' + values + ')'
    id = exec_insert_update_delete_query(query, query_parameters)
    info['id'] = id
    return info


def save_follow(required_params):
    exec_insert_update_delete_query('insert into Followers (follower , followee) values (%s , %s)',
                              (required_params['follower'], required_params['followee'],))
    return get_user_details(required_params['follower']) #email


def remove_follow(required_params):
    exec_insert_update_delete_query('delete from Followers where follower = %s and followee = %s',
                          (required_params['follower'], required_params['followee'],))
    return get_user_details(required_params['follower'])


def update_user(required_params):
    exec_insert_update_delete_query('update Users set name = %s , about = %s where email = %s',
                                    (required_params['name'], required_params['about'], required_params['user'],))
    return get_user_details(required_params['user'])
