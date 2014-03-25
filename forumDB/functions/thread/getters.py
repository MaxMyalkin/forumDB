from forumDB.functions.forum.forum_functions import get_forum_details
from forumDB.functions.user.getters import get_user_details

__author__ = 'maxim'


def get_main_info(thread):
    if not thread is None:
        return {
            'date': str(thread[0]),
            'forum': thread[2],
            'id': thread[3],
            'isClosed': bool(thread[4]),
            'isDeleted': bool(thread[5]),
            'message': thread[7],
            'slug': thread[10],
            'title': thread[11],
            'user': thread[12],

        }
    else:
        return None


def get_thread_details(thread, related):
    if not thread is None:
        info = {
            'date': get_date(thread),
            'dislikes': get_dislikes(thread),
            'forum': get_forum(thread),
            'id': get_id(thread),
            'isClosed': get_isClosed(thread),
            'isDeleted': get_isDeleted(thread),
            'likes': get_likes(thread),
            'message': get_message(thread),
            'points': get_points(thread),
            'posts': get_posts(thread),
            'slug': get_slug(thread),
            'title': get_title(thread),
            'user': get_user(thread)
        }
        if related is not None:
            for element in related:
                if element == 'user':
                    info['user'] = get_user_details(get_user(thread))
                if element == 'forum':
                    info['forum'] = get_forum_details(get_forum(thread), [])
        return info
    else:
        return None


def get_date(thread):
    if thread is not None:
        return str(thread[0])
    return None


def get_dislikes(thread):
    if thread is not None:
        return int(thread[1])
    return None


def get_forum(thread):
    if thread is not None:
        return thread[2]
    return None


def get_id(thread):
    if thread is not None:
        return int(thread[3])
    return None


def get_isClosed(thread):
    if thread is not None:
        return bool(thread[4])
    return None


def get_isDeleted(thread):
    if thread is not None:
        return bool(thread[5])
    return None


def get_likes(thread):
    if thread is not None:
        return int(thread[6])
    return None

def get_message(thread):
    if thread is not None:
        return thread[7]
    return None


def get_points(thread):
    if thread is not None:
        return int(thread[8])
    return None


def get_posts(thread):
    if thread is not None:
        return int(thread[9])
    return None


def get_slug(thread):
    if thread is not None:
        return thread[10]
    return None


def get_title(thread):
    if thread is not None:
        return thread[11]
    return None


def get_user(thread):
    if thread is not None:
        return thread[12]
    return None