import json
from django.http import HttpResponse
from forumDB.functions.common import response
from forumDB.functions.forum_functions import *

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        try:
            name = request_data['name']
            short_name = request_data['short_name']
            user = request_data['user']
        except KeyError:
            return HttpResponse(status=400)
        response_data = save_forum(name, short_name, user)
        return response(response_data)
    return HttpResponse(status=400)


def details(request):
     if request.method == 'POST':  # -------------------------to GET ---------------------------
        request_data = json.loads(request.body)
        try:
            short_name = request_data['short_name']
        except KeyError:
            return HttpResponse(status=400)
        try:
            related = request_data['related']
        except KeyError:
            related = []
        response_data = get_forum_details(short_name, related)
        return response(response_data)
     return HttpResponse(status=400)


def listThreads(request):
     if request.method == 'POST':  # -------------------------to GET ---------------------------
        request_data = json.loads(request.body)
        try:
            short_name = request_data['forum']
        except KeyError:
            return HttpResponse(status=400)
        try:
            since = request_data['since']
        except KeyError:
            since = '0000-00-00 00:00:00'

        try:
            related = request_data['related']
        except KeyError:
            related = None

        try:
            limit = request_data['limit']
        except KeyError:
            limit = None

        try:
            order = request_data['order']
        except KeyError:
            order = 'desc'

        response_data = get_listThreads( 'forum' ,short_name , since , related , limit , order)
        return response(response_data)
     return HttpResponse(status=400)