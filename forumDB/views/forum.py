import json
from django.http import HttpResponse
from forumDB.functions.common import response, get_optional_parameters
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
            related = request_data['related']
        except KeyError:
            related = None

        optional_parameters = get_optional_parameters(request_data , 'since')
        response_data = get_listThreads( 'forum' ,short_name , related , optional_parameters)
        return response(response_data)
     return HttpResponse(status=400)