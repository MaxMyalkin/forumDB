from forumDB.functions.common import find
from forumDB.functions.database import execInsertUpdateQuery
from forumDB.functions.forum.getters import get_forum_details
from forumDB.functions.user.getters import get_user_details


__author__ = 'maxim'


def save_forum(required_params):
    creator = get_user_details(required_params['user'])
    if creator is None:
        return None
    existed_forum = find('user', None, required_params['short_name'])
    if existed_forum is None:
        execInsertUpdateQuery('insert into Forums (name , short_name , user ) values (%s , %s , %s)',
                              [required_params['name'],required_params['short_name'],required_params['user']])
    return get_forum_details(required_params['short_name'], [])


