from django.http import HttpResponse
from forumDB.functions.common import make_required, make_optional, find, response_error, response_ok
from forumDB.functions.post.getters import get_post_details, get_post_list
from forumDB.functions.post.post_functions import create_post, post_vote, post_update, post_remove_restore

__author__ = 'maxim'

def create(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['date', 'thread', 'message', 'user', 'forum'])
            optional_parameters = make_optional("POST", request,
                                                ['parent', 'isApproved', 'isHighlighted', 'isEdited', 'isSpam',
                                                 'isDeleted'])
            response_data = create_post(required_params, optional_parameters)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def details(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['post'])
            optional_parameters = make_optional("GET", request,
                                                ['related'])
            response_data = get_post_details(find('post', None , required_params['post']), optional_parameters['related'])
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def vote(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['vote', 'post'])
            response_data = post_vote(required_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def update(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['message', 'post'])
            response_data = post_update(required_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def remove(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['post'])
            response_data = post_remove_restore(required_params, 'remove')
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def restore(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['post'])
            response_data = post_remove_restore(required_params, 'restore')
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def list(request):
    if request.method == 'GET':
        try:
            try:
                required_params = make_required("GET", request, ['forum'])
                required_params['type'] = 'forum'
            except Exception:
                    required_params = make_required("GET", request, ['thread'])
                    required_params['type'] = 'thread'

            optional_params = make_optional("GET", request,['since','limit', 'order'])
            response_data = get_post_list(required_params,optional_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')
