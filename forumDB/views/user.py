import json
from django.http import HttpResponse
from forumDB.functions.common import response, get_optional_parameters, make_required
from forumDB.functions.user.user_functions import *

__author__ = 'maxim'


def create(request):        # +++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params =  make_required(request_data,['email','name','username','about'])
        if required_params is None:
            return HttpResponse(status=400)
        try:
            anonymous = int(request_data['isAnonymous'])
        except KeyError:
            anonymous = 0
        response_data = save_user( required_params , anonymous)
        return response(response_data)
    else:
        return HttpResponse(status=400)


def follow(request): # +++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params =  make_required(request_data,['follower','followee'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = save_follow(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def unfollow(request): # +++++++
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params =  make_required(request_data,['follower','followee'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = remove_follow(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def details(request):   # +++++++
    if request.method == 'POST':  # ----------------------------fix to GET-------------------------------
        #email = request.GET.get('email')
        request_data = json.loads(request.body)
        required_params = make_required(request_data, ['user'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = get_user_details(request_data['user'])
        return response(response_data)
    return HttpResponse(status=400)


def list_followers(request): # +++++++
    if request.method == 'POST':  # ----------------------------fix to GET-------------------------------
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['user'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = get_list_followers(required_params,get_optional_parameters(request_data , 'since_id'))
        return response(response_data)
    return HttpResponse(status=400)


def list_following(request):  # +++++++
    if request.method == 'POST':  # ----------------------------fix to GET-------------------------------
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['user'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = get_list_following(required_params,get_optional_parameters(request_data , 'since_id'))
        return response(response_data)
    return HttpResponse(status=400)


def update(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['user', 'name' , 'about'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = update_user(required_params)
        return response(response_data)
    return HttpResponse(status=400)