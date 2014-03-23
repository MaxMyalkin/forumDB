import json
from django.http import HttpResponse
from forumDB.functions.common import response
from forumDB.functions.user_functions import *

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            email = request_data['email']
            name = request_data['name']
            username = request_data['username']
            about = request_data['about']
        except KeyError:
            return HttpResponse(status=400)
        try:
            anonymous = int(request_data['isAnonymous'])
        except KeyError:
            anonymous = 0
        response_data = save_user(email, name, username, about, anonymous)
        return response(response_data)
    else:
        return HttpResponse(status=400)


def follow(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            follower = request_data['follower']
            followee = request_data['followee']
        except KeyError:
            return HttpResponse(status=400)
        response_data = save_follow(follower, followee)
        return response(response_data)
    return HttpResponse(status=400)


def unfollow(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            follower = request_data['follower']
            followee = request_data['followee']
        except KeyError:
            return HttpResponse(status=400)
        response_data = remove_follow(follower, followee)
        return response(response_data)
    return HttpResponse(status=400)


def details(request):
    if request.method == 'POST':  # ----------------------------fix to GET-------------------------------
        #email = request.GET.get('email')
        request_data = json.loads(request.body)
        try:
            email = request_data['user']
        except KeyError:
            return HttpResponse(status=400)
        response_data = get_user_details(email)
        return response(response_data)
    return HttpResponse(status=400)


def list_followers(request):
    if request.method == 'POST':  # ----------------------------fix to GET-------------------------------
        request_data = json.loads(request.body)
        try:
            email = request_data['user']
        except KeyError:
            HttpResponse(status=400)

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
        return response(response_data)
    return HttpResponse(status=400)


def list_following(request):
    if request.method == 'POST':  # ----------------------------fix to GET-------------------------------
        request_data = json.loads(request.body)
        try:
            email = request_data['user']
        except KeyError:
            return HttpResponse(status=400)

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
        return response(response_data)
    return HttpResponse(status=400)


def update(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            email = request_data['user']
            name = request_data['name']
            about = request_data['about']
        except KeyError:
            return HttpResponse(status=400)
        response_data = update_user(email, name, about)
        return response(response_data)
    return HttpResponse(status=400)