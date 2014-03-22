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
    existed_user = execSelectQuery('select about , email , id , isAnonymous , name , username from Users where email = %s' , [email])
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
