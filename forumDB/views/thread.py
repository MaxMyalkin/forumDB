from django.http import HttpResponse
from forumDB.functions.common import response, find, make_required, make_optional
from forumDB.functions.forum.getters import get_listThreads
from forumDB.functions.thread.thread_functions import close_or_open, thread_vote, get_thread_details, unsubscribe_thread, subscribe_thread, save_thread, thread_update

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        required_params = make_required("POST", request,
                                        ['forum', 'title', 'isClosed', 'user', 'date', 'message', 'slug'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_params = make_optional("POST", request, ['isDeleted'])
        response_data = save_thread(required_params, optional_params)
        return response(response_data)
    return HttpResponse(status=400)


def subscribe(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['user', 'thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = subscribe_thread(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def unsubscribe(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['user', 'thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = unsubscribe_thread(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def details(request):
    if request.method == 'GET':
        required_params = make_required("GET", request, ['thread'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_params = make_optional("GET", request, ['related'])
        response_data = get_thread_details(find('thread', 'id', required_params['thread']), optional_params['related'])
        return response(response_data)
    return HttpResponse(status=400)


def vote(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['vote', 'thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = thread_vote(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def open(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = close_or_open('open', required_params['thread'])
        return response(response_data)
    return HttpResponse(status=400)


def close(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['thread'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = close_or_open('close', required_params['thread'])
        return response(response_data)
    return HttpResponse(status=400)


def list(request):
    if request.method == 'GET':
        user = None
        forum = None
        try:
            user = request.GET.get('user')
        except KeyError:
            pass

        try:
            forum = request.GET.get('forum')
        except KeyError:
            pass

        optional_parameters = make_optional("GET", request, ['since', 'limit', 'order'])
        if user is None:
            if forum is None:
                return HttpResponse(status=400)
            else:
                response_data = get_listThreads('forum', forum, [], optional_parameters)
        else:
            response_data = get_listThreads('user', user, [], optional_parameters)
        return response(response_data)
    return HttpResponse(status=400)


def update(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['message', 'thread', 'slug'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = thread_update(required_params)
        return response(response_data)
    return HttpResponse(status=400)