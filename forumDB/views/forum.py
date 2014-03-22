import json
from django.http import HttpResponse
from forumDB.database import execSelectQuery, execInsertUpdateQuery

__author__ = 'maxim'

def create(request):
    if(request.method == 'POST'):
        request_data = json.loads(request.body)
        name = request_data['name']
        short_name = request_data['short_name']
        user = request_data['user']
        response_data = saveForum(name , short_name , user)
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    else:
        return HttpResponse(status=400)


def saveForum(name , short_name , user):
    existed_user = execSelectQuery('select id , name , short_name , user from Forums where  = %s', [short_name])
    if(len(existed_user) == 0):
        execInsertUpdateQuery('insert into Forums (name , short_name , user ) values (%s , %s , %s)',
                          [name, short_name, user])
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
