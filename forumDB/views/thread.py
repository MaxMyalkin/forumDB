import json
from django.http import HttpResponse
from forumDB.functions.thread_functions import *

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        forum = request_data['forum']
        title = request_data['title']
        isClosed = int(request_data['isClosed'])
        user = request_data['user']
        date = request_data['date']
        message = request_data['message']
        slug = request_data['slug']
        try:
            isDeleted = int(request_data['isDeleted'])
        except KeyError:
            isDeleted = 0
        response_data = save_thread(forum, title, isClosed, user, date, message, slug, isDeleted)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)


def subscribe(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        user = request_data['user']
        thread = request_data['thread']
        response_data = subscribe_thread(user , thread)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)


def unsubscribe(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        user = request_data['user']
        thread = request_data['thread']
        response_data = unsubscribe_thread(user , thread)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)