import json
from django.http import HttpResponse
from forumDB.functions.database import execSelectQuery

__author__ = 'maxim'


def response(response_data):
    if response_data is not None:
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    else:
        return HttpResponse(status=400)


def get_optional_parameters(request_data, since):
    parameters = {}
    if since == 'since':
        try:
            parameters['since'] = request_data['since']
        except KeyError:
            parameters['since'] = '0000-00-00 00:00:00'
    else:
        try:
            parameters['since'] = request_data['since_id']
        except KeyError:
            parameters['since'] = 0
    try:
        parameters['limit'] = request_data['limit']
    except KeyError:
        parameters['limit'] = None

    try:
        parameters['order'] = request_data['order']
    except KeyError:
        parameters['order'] = 'desc'
    return parameters


def find(what, type, value):
    object = None
    if what == 'user':
        object = execSelectQuery(
            'select about , email , id , isAnonymous , name , username from Users where email = %s',
            [value])
    if what == 'forum':
        object = execSelectQuery('select id, name , short_name , user  from Forums where short_name = %s',
                                 [value])
    if what == 'thread':
        object = execSelectQuery(
            'select date, dislikes , forum , id , isClosed , isDeleted , likes , message ,points , posts, slug , title , '
            'user  from Threads where ' + type + ' = %s', [value])


    if len(object) == 0 or object is None:
        return None
    else:
        return object[0]