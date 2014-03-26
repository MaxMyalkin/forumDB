from django.http import HttpResponse
from forumDB.functions.common import make_required, response, make_optional, find
from forumDB.functions.post.getters import get_post_details
from forumDB.functions.post.post_functions import create_post, post_vote, post_update, post_remove_restore, get_post_list

__author__ = 'maxim'

def create(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['date', 'thread', 'message', 'user', 'forum'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_parameters = make_optional("POST", request,
                                            ['parent', 'isApproved', 'isHighlighted', 'isEdited', 'isSpam',
                                             'isDeleted'])
        response_data = create_post(required_params, optional_parameters)
        return response(response_data)
    else:
        return HttpResponse(status=400)


def details(request):
    if request.method == 'GET':
        required_params = make_required("GET", request, ['post'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_parameters = make_optional("GET", request,
                                            ['related'])
        response_data = get_post_details(find('post', None , required_params['post']), optional_parameters['related'])
        return response(response_data)
    else:
        return HttpResponse(status=400)


def vote(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['vote', 'post'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = post_vote(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def update(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['message', 'post'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = post_update(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def remove(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['post'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = post_remove_restore(required_params, 'remove')
        return response(response_data)
    return HttpResponse(status=400)


def restore(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['post'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = post_remove_restore(required_params, 'restore')
        return response(response_data)
    return HttpResponse(status=400)


def list(request):
    if request.method == 'GET':
        required_params = make_required("GET", request, ['forum'])
        if required_params is None:
            required_params = make_required("GET", request, ['thread'])
            if required_params is None:
                return HttpResponse(status=400)
            else:
                required_params['type'] = 'thread'
        else:
            required_params['type'] = 'forum'
        optional_params = make_optional("GET", request,['since','limit', 'order'])
        response_data = get_post_list(required_params,optional_params)
        return response(response_data)
    else:
        return HttpResponse(status=400)
