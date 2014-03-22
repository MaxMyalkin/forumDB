import json
from django.http import HttpResponse
from forumDB.functions.forum_functions import save_forum

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        name = request_data['name']
        short_name = request_data['short_name']
        user = request_data['user']
        response_data = save_forum(name, short_name, user)
        if response_data is None:
            return HttpResponse(status=400)
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    else:
        return HttpResponse(status=400)
