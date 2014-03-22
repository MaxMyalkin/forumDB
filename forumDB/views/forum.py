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
        response_data = saveForum(name, short_name, user)
        if(response_data == None):
            return HttpResponse(status=400)
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    else:
        return HttpResponse(status=400)


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
