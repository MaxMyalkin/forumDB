import json
from django.http import HttpResponse
from forumDB.functions.common import response, make_required, make_optional
from forumDB.functions.user.user_functions import *

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['email', 'name', 'username', 'about'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_parameters = make_optional("POST", request, ['isAnonymous'])
        response_data = create_user(required_params, optional_parameters)
        return response(response_data)
    else:
        return HttpResponse(status=400)


def follow(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['follower', 'followee'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = save_follow(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def unfollow(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['follower', 'followee'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = remove_follow(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def details(request):
    if request.method == 'GET':
        required_params = make_required("GET", request, ['user'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = get_user_details(required_params['user'])
        return response(response_data)
    return HttpResponse(status=400)


def list_followers(request):
    if request.method == 'GET':
        required_params = make_required("GET", request, ['user'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_parameters = make_optional("GET", request, ['limit', 'since_id', 'order'])
        response_data = get_list_followers(required_params, optional_parameters)
        return response(response_data)
    return HttpResponse(status=400)


def list_following(request):
    if request.method == 'GET':
        required_params = make_required("GET" , request, ['user'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_parameters = make_optional("GET", request, ['limit', 'since_id', 'order'])
        response_data = get_list_following(required_params, optional_parameters)
        return response(response_data)
    return HttpResponse(status=400)


def update(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['user', 'name', 'about'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = update_user(required_params)
        return response(response_data)
    return HttpResponse(status=400)