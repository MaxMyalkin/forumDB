import json
from django.http import HttpResponse
from forumDB.functions.forum_functions import *

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        name = request_data['name']
        short_name = request_data['short_name']
        user = request_data['user']
        response_data = save_forum(name, short_name, user)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)


def details(request):
     if request.method == 'POST':  # -------------------------to GET ---------------------------
        request_data = json.loads(request.body)
        short_name = request_data['short_name']
        try:
            related = request_data['related']
        except KeyError:
            related = []
        response_data = get_forum_details(short_name, related)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
     return HttpResponse(status=400)