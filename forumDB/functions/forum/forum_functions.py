from forumDB.functions.database import exec_insert_update_delete_query
__author__ = 'maxim'


def create_forum(required_params):
    id = exec_insert_update_delete_query('insert into Forums (name , short_name , user ) values (%s , %s , %s)',
                          ( required_params['name'], required_params['short_name'], required_params['user'],))
    info = {
        'name': required_params['name'],
        'short_name': required_params['short_name'],
        'user': required_params['user'],
        'id': id
    }
    return info


