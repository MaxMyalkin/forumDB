import json
from django.http import HttpResponse
from forumDB.functions.database import execSelectQuery

__author__ = 'maxim'


def response_ok(response_data):
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')


def response_error(response_data):
        return HttpResponse(json.dumps({'code': 1, 'message': response_data}), content_type='application/json')


def make_optional( request_type , request, parameters):
    optional_parameters = {}
    if request_type == "POST":
        request_data = json.loads(request.body)
        for parameter in parameters:
            try:
                optional_parameters[parameter] = request_data[parameter].encode('utf-8')
            except KeyError:
                optional_parameters[parameter] = None
            except Exception:
                optional_parameters[parameter] = request_data[parameter]
    if request_type == "GET":
        for parameter in parameters:
            try:
                optional_parameters[parameter] = request.GET.get(parameter).encode('utf-8')
            except KeyError:
                optional_parameters[parameter] = None
            except Exception:
                optional_parameters[parameter] = request.GET.get('utf-8')

    return optional_parameters


def make_required( request_type , request, parameters):
    required_parameters = {}
    if request_type == "POST":
        request_data = json.loads(request.body)
        for parameter in parameters:
            try:
                required_parameters[parameter] = request_data[parameter].encode('utf-8')
            except KeyError:
                raise Exception('you should set parameter "' + parameter+'"')
            except Exception:
                required_parameters[parameter] = request_data[parameter]

    if request_type == "GET":
        for parameter in parameters:
            try:
                required_parameters[parameter] = request.GET.get(parameter).encode('utf-8')
            except Exception:
                required_parameters[parameter] = request.GET.get(parameter)
            if required_parameters[parameter] is None:
                raise Exception('you should set parameter "' + parameter + '"')
    return required_parameters


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

    if what == 'post':
        object = execSelectQuery('select date , dislikes , forum , id , isApproved , isDeleted , isEdited , '
                                 'isHighlighted , isSpam , likes , message , parent , points , thread , user from Posts'
                                 ' where id = %s ', [value])

    if len(object) == 0 or object is None:
        raise Exception(what + ' with ' + value + ' parameter doesnt exist')
    else:
        return object[0]