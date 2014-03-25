import json
from django.http import HttpResponse
from forumDB.functions.common import response, get_optional_parameters, find, make_required
from forumDB.functions.forum.getters import get_listThreads
from forumDB.functions.thread.thread_functions import close_or_open, thread_vote, get_thread_details, unsubscribe_thread, subscribe_thread, save_thread, thread_update

__author__ = 'maxim'


def create(request):  #++++++++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['forum' , 'title' , 'isClosed' , 'user' , 'date' , 'message' , 'slug'])
        if required_params is None:
            return HttpResponse(status=400)
        try:
            isDeleted = int(request_data['isDeleted'])
        except KeyError:
            isDeleted = 0
        response_data = save_thread(required_params, isDeleted)
        return response(response_data)
    return HttpResponse(status=400)


def subscribe(request): #++++++++++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['user' , 'thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = subscribe_thread(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def unsubscribe(request): #++++++++++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['user' , 'thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = unsubscribe_thread(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def details(request): #++++++++++++++
    if request.method == 'POST':  # -------------------------- to GET-------------------------------------
        request_data = json.loads(request.body)
        user = None
        forum = None
        required_params = make_required(request_data , ['thread'])
        if required_params is None:
            return HttpResponse(status=400)
        try:
            for el in request_data['related']:
                if el == 'user':
                    user = 'ok'
                if el == 'forum':
                    forum = 'ok'
        except KeyError:
            pass
        response_data = get_thread_details(find('thread', 'id', required_params['thread']), user, forum)
        return response(response_data)
    return HttpResponse(status=400)


def vote(request):  #+++++++++++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['vote' , 'thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = thread_vote(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def open(request): #+++++++++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = close_or_open('open', required_params['thread'])
        return response(response_data)
    return HttpResponse(status=400)


def close(request):  #+++++++++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = close_or_open('close', required_params['thread'])
        return response(response_data)
    return HttpResponse(status=400)


def list(request): #+++++++++++++++++
    if request.method == 'POST':  #--------------------------------to Get------------------------------
        request_data = json.loads(request.body)
        user = None
        forum = None
        try:
            user = request_data['user']
        except KeyError:
            pass

        try:
            forum = request_data['forum']
        except KeyError:
            pass

        optional_parameters = get_optional_parameters(request_data, 'since')

        if user is None:
            if forum is None:
                return HttpResponse(status=400)
            else:
                response_data = get_listThreads('forum', forum, [], optional_parameters)
        else:
            response_data = get_listThreads('user', user, [], optional_parameters)
        return response(response_data)
    return HttpResponse(status=400)


def update(request):  #+++++++++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['message' , 'thread' , 'slug'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = thread_update(required_params)
        return response(response_data)
    return HttpResponse(status=400)