from forumDB.functions.database import execSelectQuery, execInsertUpdateQuery

__author__ = 'maxim'

def saveUser(email , name , username , about , anonymous):
    existed_user = find_user(email)
    if(existed_user == None):
        execInsertUpdateQuery('insert into Users (email , name , username , about , isAnonymous ) values (%s , %s , %s , %s , %s)',
                          [email, name, username, about, anonymous])
        return getMainInfo(find_user(email))
    else:
        return getMainInfo(existed_user)

def find_user(email):
    user = execSelectQuery('select about , email , id , isAnonymous , name , username from Users where email = %s' , [email])
    if len(user) == 0:
        return None
    else:
        return user

def saveFollow(follower , followee):
    follower_user = find_user(follower)
    followee_user = find_user(followee)
    if(not follower_user == None and not followee_user == None):
        existed_follow = execSelectQuery('select follower , followee from Followers where follower = %s and followee =%s', [follower , followee])
        if(len(existed_follow) == 0):
            execInsertUpdateQuery('insert into Followers (follower , followee) values (%s , %s)',
                      [follower , followee])
    else:
        return None
    return getDetails(follower_user[0][1])

def removeFollow(follower , followee):
    follower_user = find_user(follower)
    followee_user = find_user(followee)
    if(not follower_user == None and not followee_user == None):
        existed_follow = execSelectQuery('select follower , followee from Followers where follower = %s and followee =%s', [follower , followee])
        if(len(existed_follow) == 1):
            execInsertUpdateQuery('delete from Followers where follower = %s and followee = %s',
                      [follower , followee])
            return getDetails(follower_user[0][1])# email
    return None

def getDetails(email):
    user = find_user(email)
    if(user == None):
        return None
    info = getMainInfo(user)
    info['followers'] = getFollows('follower',email)
    info['following'] = getFollows('followee' , email)
    return info


def getFollows(what , email ):   #get following or followers
    list = []
    if(what == 'following'):
        for element in execSelectQuery('select followee from Followers where follower = %s', [email]):
            list.append(element[0])
    else:
        for element in execSelectQuery('select follower from Followers where followee = %s',[email]):
            list.append(element[0])
    return list


def updateUser(email , name , about):
    pass


def getMainInfo(user):
    if(not user == None):
        return {
                'about': user[0][0],
                'email': user[0][1],
                'id':user[0][2],
                'isAnonymous': user[0][3],
                'name':user[0][4],
                'username':user[0][5]
        }
    else:
        return None