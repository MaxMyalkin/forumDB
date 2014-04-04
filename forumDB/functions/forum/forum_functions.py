from forumDB.functions.common import find
from forumDB.functions.database import execInsertUpdateQuery
from forumDB.functions.forum.getters import get_forum_details
__author__ = 'maxim'


def create_forum(required_params):
    find('user', None, required_params['user'])
    try:
        existed_forum = find('forum', None, required_params['short_name'])
    except Exception:
        existed_forum = None
    if existed_forum is None:
        execInsertUpdateQuery('insert into Forums (name , short_name , user ) values (%s , %s , %s)',
                              (required_params['name'], required_params['short_name'], required_params['user'],))
    return get_forum_details(required_params['short_name'], [])


