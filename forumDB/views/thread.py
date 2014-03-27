from django.http import HttpResponse
from forumDB.functions.common import find, make_required, make_optional, response_error, response_ok
from forumDB.functions.forum.getters import get_listThreads
from forumDB.functions.post.getters import get_thread_post_list
from forumDB.functions.thread.thread_functions import close_or_open, thread_vote, get_thread_details, unsubscribe_thread, subscribe_thread, create_thread, thread_update, thread_remove_restore

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request,
                                            ['forum', 'title', 'isClosed', 'user', 'date', 'message', 'slug'])
            optional_params = make_optional("POST", request, ['isDeleted'])
            response_data = create_thread(required_params, optional_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def subscribe(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['user', 'thread'])
            if required_params is None:
                return HttpResponse(status=400)
            response_data = subscribe_thread(required_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def unsubscribe(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['user', 'thread'])
            response_data = unsubscribe_thread(required_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def details(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['thread'])
            optional_params = make_optional("GET", request, ['related'])
            response_data = get_thread_details(find('thread', 'id', required_params['thread']), optional_params['related'])
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def vote(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['vote', 'thread'])
        response_data = thread_vote(required_params)
        return response_ok(response_data)
    return response_error('incorrect type of request')


def open(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['thread'])
            response_data = close_or_open('open', required_params['thread'])
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def close(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['thread'])
            response_data = close_or_open('close', required_params['thread'])
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def list(request):
    if request.method == 'GET':
        try:
            user = request.GET.get('user')
            forum = request.GET.get('forum')
            optional_parameters = make_optional("GET", request, ['since', 'limit', 'order'])
            if user is None:
                if forum is None:
                    response_error('you should set "user" or "forum"')
                else:
                    response_data = get_listThreads('forum', forum, [], optional_parameters)
            else:
                response_data = get_listThreads('user', user, [], optional_parameters)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def update(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['message', 'thread', 'slug'])
            response_data = thread_update(required_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def list_posts(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['thread'])
            optional_params = make_optional("GET", request, ['since', 'limit', 'order'])
            response_data = get_thread_post_list(required_params,optional_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def remove(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['thread'])
            response_data = thread_remove_restore(required_params, 'remove')
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def restore(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['thread'])
            response_data = thread_remove_restore(required_params, 'restore')
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')