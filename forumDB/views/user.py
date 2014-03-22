import json
from django.http import HttpResponse
from forumDB.functions.user_functions import *

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        email = request_data['email']
        name = request_data['name']
        username = request_data['username']
        about = request_data['about']
        try:
            anonymous = int(request_data['isAnonymous'])
        except KeyError:
            anonymous = 0
        response_data = save_user(email, name, username, about, anonymous)
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    else:
        return HttpResponse(status=400)


def follow(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        follower = request_data['follower']
        followee = request_data['followee']
        response_data = save_follow(follower, followee)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)


def unfollow(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        follower = request_data['follower']
        followee = request_data['followee']
        response_data = remove_follow(follower, followee)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)


def details(request):
    if request.method == 'POST':  # ----------------------------fix to GET-------------------------------
        #email = request.GET.get('email')
        request_data = json.loads(request.body)
        email = request_data['user']
        response_data = get_details(email)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)


def list_followers(request):
    if request.method == 'POST':  # ----------------------------fix to GET-------------------------------
        request_data = json.loads(request.body)
        email = request_data['user']

        try:
            since = request_data['since_id']
        except KeyError:
            since = 0

        try:
            limit = request_data['limit']
        except KeyError:
            limit = None

        try:
            order = request_data['order']
        except KeyError:
            order = 'desc'

        response_data = get_list_followers(email, limit, since, order)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)


def list_following(request):
    if request.method == 'POST':  # ----------------------------fix to GET-------------------------------
        request_data = json.loads(request.body)
        email = request_data['user']
        try:
            since = request_data['since_id']
        except KeyError:
            since = 0

        try:
            limit = request_data['limit']
        except KeyError:
            limit = None

        try:
            order = request_data['order']
        except KeyError:
            order = 'desc'

        response_data = get_list_following(email, limit, since, order)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)


def update(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        email = request_data['user']
        name = request_data['name']
        about = request_data['about']
        response_data = update_user(email, name, about)
        if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)