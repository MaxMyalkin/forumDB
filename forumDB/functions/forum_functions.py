from forumDB.functions.database import execSelectQuery, execInsertUpdateQuery

__author__ = 'maxim'

def saveForum(name, short_name, user):
    creator = execSelectQuery('select email from Users where email = %s', [user])
    if(len(creator) == 0):
        return None
    existed_forum = execSelectQuery('select id , name , short_name , user from Forums where short_name = %s', [short_name])
    if(len(existed_forum) == 0):
        execInsertUpdateQuery('insert into Forums (name , short_name , user ) values (%s , %s , %s)',
                          [name, short_name, user])
        id = execSelectQuery('select id from Forums where short_name = %s', [short_name])[0][0]
    else:
        id = existed_forum[0][0]
        name = existed_forum[0][1]
        short_name = existed_forum[0][2]
        user = existed_forum[0][3]

    return {
        'id': id,
        'name': name,
        'short_name':short_name,
        'user': user
    }
