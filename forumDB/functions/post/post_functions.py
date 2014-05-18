from forumDB.functions.database import exec_insert_update_delete_query
from forumDB.functions.post.getters import get_post_main

__author__ = 'maxim'


def create_post(required_parameters, optional_parameters):
    info = {
        'date': required_parameters['date'],
        'thread': required_parameters['thread'],
        'message': required_parameters['message'],
        'user': required_parameters['user'],
        'forum': required_parameters['forum']
    }
    query = 'insert into Posts (date , thread , message , user , forum '
    values = "( %s , %s , %s , %s , %s "
    query_parameters = [required_parameters['date'], required_parameters['thread'],
                        required_parameters['message'],
                        required_parameters['user'], required_parameters['forum']]

    for parameter in optional_parameters:
        if optional_parameters[parameter] is not None:
            query += ',' + parameter
            values += ', %s '
            query_parameters.append(optional_parameters[parameter])
            info[parameter] = optional_parameters[parameter]

    query += ') values ' + values + ')'

    info['id'] = exec_insert_update_delete_query(query, query_parameters)

    exec_insert_update_delete_query('update Threads set posts = posts + 1 where id = %s',
                          (required_parameters['thread'],))
    return info


def post_vote(required_params):
    if required_params['vote'] == 1:
        exec_insert_update_delete_query(
            'update Posts set likes = likes + 1 , points = likes - dislikes where id = %s', (required_params['post'],))
    if required_params['vote'] == -1:
        exec_insert_update_delete_query(
            'update Posts set dislikes = dislikes + 1, points = likes - dislikes where id = %s',
            (required_params['post'],))
    return get_post_main(required_params['post'])


def post_update(required_params):
    exec_insert_update_delete_query("update Posts set message = %s where id = %s",
                          (required_params['message'], required_params['post'],))
    return get_post_main(required_params['post'])


def post_remove_restore(required_params, type):
    id = 0
    if type == 'remove':
        id = exec_insert_update_delete_query("update Posts set isDeleted = 1 where id = %s", (required_params['post'],))
    if type == 'restore':
        id = exec_insert_update_delete_query("update Posts set isDeleted = 0 where id = %s", (required_params['post'],))
    return {'post': id}