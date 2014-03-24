from forumDB.functions.common import find
from forumDB.functions.database import execInsertUpdateQuery
from forumDB.functions.forum.getters import get_forum_details
from forumDB.functions.user.getters import get_user_details


__author__ = 'maxim'


def save_forum(name, short_name, user):
    creator = get_user_details(user)
    if creator is None:
        return None
    existed_forum = find('user', None, short_name)
    if existed_forum is None:
        execInsertUpdateQuery('insert into Forums (name , short_name , user ) values (%s , %s , %s)',
                              [name, short_name, user])
    return get_forum_details(short_name, [])


