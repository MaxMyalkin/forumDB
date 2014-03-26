from forumDB.functions.common import find
from forumDB.functions.database import execInsertUpdateQuery, execSelectQuery
from forumDB.functions.forum.getters import get_forum_details
from forumDB.functions.post.getters import get_post_main, get_post_details

__author__ = 'maxim'


def create_post(required_parameters, optional_parameters):
    user = find('user', None, required_parameters['user'])
    forum = find('forum', None, required_parameters['forum'])
    thread = find('thread', 'id', required_parameters['thread'])
    if user is not None and forum is not None and thread is not None:
        threads_of_forum = execSelectQuery('select id from Threads where forum = %s',
                                           [required_parameters['forum']])
        for parameter in threads_of_forum:
            if parameter[0] == int(required_parameters['thread']):
                query = 'insert into Posts (date , thread , message , user , forum '
                values = "( %s , %s , %s , %s , %s "
                query_parameters = [required_parameters['date'], required_parameters['thread'],
                                    required_parameters['message'],
                                    required_parameters['user'], required_parameters['forum']]

                if optional_parameters['parent'] is not None:
                    parent = execSelectQuery('select id from Posts where thread = %s and id = %s',
                                             [required_parameters['thread'], optional_parameters['parent']])
                    if len(parent) == 0:
                        return None

                for parameter in optional_parameters:
                    if optional_parameters[parameter] is not None:
                        query += ',' + parameter
                        values += ', %s '
                        query_parameters.append(optional_parameters[parameter])

                query += ') values ' + values + ')'
                post_id = execInsertUpdateQuery(query, query_parameters)
                execInsertUpdateQuery('update Threads set posts = posts + 1 where id = %s',[required_parameters['thread']])
                return get_post_main(find('post', None, post_id))
    else:
        return None


def post_vote(required_params):
    if required_params['vote'] == 1:
        execInsertUpdateQuery(
            'update Posts set likes = likes + 1 , points = likes - dislikes where id = %s', [required_params['post']])
    if required_params['vote'] == -1:
        execInsertUpdateQuery(
            'update Posts set dislikes = dislikes + 1, points = likes - dislikes where id = %s', [required_params['post']])
    return get_post_details(find('post', None, required_params['post']), [])


def post_update(required_params):
        execInsertUpdateQuery("update Posts set message = %s where id = %s" , [required_params['message'], required_params['post']])
        return get_post_details(find('post', None, required_params['post']), [])


def post_remove_restore(required_params , type):
    if type == 'remove':
        execInsertUpdateQuery("update Posts set isDeleted = 1 where id = %s" , [required_params['post']])
    if type == 'restore':
        execInsertUpdateQuery("update Posts set isDeleted = 0 where id = %s" , [required_params['post']])
    post = get_post_details(find('post', None, required_params['post']), [])
    if post is not None:
        return {'post': post['id']}
    else:
        return None

