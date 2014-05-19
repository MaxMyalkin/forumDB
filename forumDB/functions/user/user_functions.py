from forumDB.functions.database import exec_insert_update_delete_query
from forumDB.functions.user.getters import get_user_details
import MySQLdb as mDB

__author__ = 'maxim'

host = 'localhost'
user = 'maxim'
password = '12345'
database = 'forumDB_ID'


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
    db = mDB.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()

    query = """select id from Users where email = %s"""

    cursor.execute(query, (required_params['follower'],))
    id = cursor.fetchone()
    follower = id[0]

    cursor.execute(query, (required_params['followee'],))
    id = cursor.fetchone()
    followee = id[0]

    exec_insert_update_delete_query("""insert into Followers (follower , followee) values (%s, %s)""",
                                    (follower, followee,))

    cursor.close()
    db.close()


    return get_user_details(follower, 'id')


def remove_follow(required_params):
    #index follower followee

    db = mDB.connect(host, user, password, database, init_command='SET NAMES UTF8')
    cursor = db.cursor()

    query = """select id from Users where email = %s"""

    cursor.execute(query, (required_params['follower'],))
    id = cursor.fetchone()
    follower = id[0]

    cursor.execute(query, (required_params['followee'],))
    id = cursor.fetchone()
    followee = id[0]

    exec_insert_update_delete_query("""delete from Followers
                                        where follower = %s and followee = %s""",
                                    (follower, followee,))

    cursor.close()
    db.close()

    return get_user_details(follower, 'id')


def update_user(required_params):
    exec_insert_update_delete_query('update Users set name = %s , about = %s where email = %s',
                                    (required_params['name'], required_params['about'], required_params['user'],))
    return get_user_details(required_params['user'], 'email')
