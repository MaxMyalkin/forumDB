import json
from django.http import HttpResponse
from forumDB.functions.common import response
from forumDB.functions.thread_functions import *

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            forum = request_data['forum']
            title = request_data['title']
            isClosed = int(request_data['isClosed'])
            user = request_data['user']
            date = request_data['date']
            message = request_data['message']
            slug = request_data['slug']
        except KeyError:
            return HttpResponse(status=400)
        try:
            isDeleted = int(request_data['isDeleted'])
        except KeyError:
            isDeleted = 0
        response_data = save_thread(forum, title, isClosed, user, date, message, slug, isDeleted)
        return response(response_data)
    return HttpResponse(status=400)


def subscribe(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            user = request_data['user']
            thread = request_data['thread']
        except KeyError:
            return HttpResponse(status=400)
        response_data = subscribe_thread(user, thread)
        return response(response_data)
    return HttpResponse(status=400)


def unsubscribe(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            user = request_data['user']
            thread = request_data['thread']
        except KeyError:
            return HttpResponse(status=400)
        response_data = unsubscribe_thread(user, thread)
        return response(response_data)
    return HttpResponse(status=400)


def details(request):
    if request.method == 'POST':  # -------------------------- to GET-------------------------------------
        request_data = json.loads(request.body)
        user = None
        forum = None
        try:
            thread = request_data['thread']
        except KeyError:
            return HttpResponse(status=400)
        try:
            for el in request_data['related']:
                if el == 'user':
                    user = 'ok'
                if el == 'forum':
                    forum = 'ok'
        except KeyError:
            pass
        response_data = get_thread_details(find_thread('id', thread), user , forum)
        return response(response_data)
    return HttpResponse(status=400)


def vote(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            thread = request_data['thread']
            vote = request_data['vote']
        except KeyError:
            return HttpResponse(status=400)
        response_data = thread_vote(thread, vote)
        return response(response_data)
    return HttpResponse(status=400)


def open(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            thread = request_data['thread']
        except KeyError:
            return HttpResponse(status=400)
        response_data = close_or_open('open', thread)
        return response(response_data)
    return HttpResponse(status=400)


def close(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            thread = request_data['thread']
        except KeyError:
            return HttpResponse(status=400)
        response_data = close_or_open('close', thread)
        return response(response_data)
    return HttpResponse(status=400)