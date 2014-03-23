from forumDB.functions.database import execSelectQuery, execInsertUpdateQuery
from forumDB.functions.user_functions import get_details

__author__ = 'maxim'


def save_forum(name, short_name, user):
    creator = get_details(user)
    if creator is None:
        return None
    existed_forum = find_forum(short_name)
    if existed_forum is None:
        execInsertUpdateQuery('insert into Forums (name , short_name , user ) values (%s , %s , %s)',
                              [name, short_name, user])
        existed_forum = find_forum(short_name)
    return get_main_info(existed_forum)



def find_forum(short_name):
    forum = execSelectQuery('select id, name , short_name , user  from Forums where short_name = %s',
                           [short_name])
    if len(forum) == 0:
        return None
    else:
        return forum[0]


def get_main_info(forum):
    if forum is not None:
        return {
            'id': forum[0],
            'name': forum[1],
            'short_name': forum[2],
            }
    else:
        return None


def get_forum_details(short_name , related):
    forum = find_forum(short_name)
    if forum is None:
        return None
    info = get_main_info(forum)
    if related == ['user',]:
        info['user'] = get_details(forum[3])
    return info