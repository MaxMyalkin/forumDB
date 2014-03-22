import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from forumDB.database import *
__author__ = 'maxim'


def create(request):
    if(request.method == 'POST'):
        request_data = json.loads(request.body)
        email = request_data['email']
        name = request_data['name']
        username = request_data['username']
        about = request_data['about']
        try:
            anonymous = int(request_data['isAnonymous'])
        except KeyError:
            anonymous = 0
        response_data = saveUser(email , name , username , about , anonymous)
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    else:
        return HttpResponse(status=400)


def saveUser(email , name , username , about , anonymous):
    existed_user = find_user(email)
    if(len(existed_user) == 0):
        execInsertUpdateQuery('insert into Users (email , name , username , about , isAnonymous ) values (%s , %s , %s , %s , %s)',
                          [email, name, username, about, anonymous])
        id = execSelectQuery('select id from Users where email = %s' , [email])[0][0]
    else:
        about = existed_user[0][0]
        email = existed_user[0][1]
        id = existed_user[0][2]
        anonymous = bool(existed_user[0][3])
        name = existed_user[0][4]
        username = existed_user[0][5]

    return {
        'about': about,
        'email': email,
        'id': id,
        'isAnonymous': anonymous,
        'name':name,
        'username': username
    }

def find_user(email):
    return execSelectQuery('select about , email , id , isAnonymous , name , username from Users where email = %s' , [email])

def follow(request):
     if(request.method == 'POST'):
        request_data = json.loads(request.body)
        follower = request_data['follower']
        followee = request_data['followee']
        response_data = saveFollow(follower, followee)
        if(response_data == None):
            return HttpResponse(status=400)
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
     else:
        return HttpResponse(status=400)

def saveFollow(follower , followee):
    follower_user = find_user(follower)
    followee_user = find_user(followee)
    if(len(follower_user) == 1 and len(followee_user) == 1):
        existed_follow = execSelectQuery('select follower , followee from Followers where follower = %s and followee =%s', [follower , followee])
        if(len(existed_follow) == 0):
            execInsertUpdateQuery('insert into Followers (follower , followee) values (%s , %s)',
                      [follower , followee])
    else:
        return None
    return {
        'about': followee_user[0][0],
        'email': followee_user[0][1],
        'id':followee_user[0][2],
        'isAnonymous': followee_user[0][3],
        'name':followee_user[0][4],
        'username':followee_user[0][5],         
    }
