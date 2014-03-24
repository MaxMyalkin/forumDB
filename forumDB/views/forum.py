import json
from django.http import HttpResponse
from forumDB.functions.common import response, get_optional_parameters, make_required
from forumDB.functions.forum.forum_functions import save_forum, get_forum_details
from forumDB.functions.forum.getters import get_listThreads

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['name' , 'short_name' , 'user'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = save_forum(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def details(request):
     if request.method == 'POST':  # -------------------------to GET ---------------------------
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['short_name'])
        if required_params is None:
            return HttpResponse(status=400)
        try:
            related = request_data['related']
        except KeyError:
            related = []
        response_data = get_forum_details(required_params['short_name'], related)
        return response(response_data)
     return HttpResponse(status=400)


def listThreads(request):
     if request.method == 'POST':  # -------------------------to GET ---------------------------
        request_data = json.loads(request.body)
        required_params = make_required(request_data , ['forum'])
        if required_params is None:
            return HttpResponse(status=400)
        try:
            related = request_data['related']
        except KeyError:
            related = None
        optional_parameters = get_optional_parameters(request_data , 'since')
        response_data = get_listThreads( 'forum' ,required_params['forum'] , related , optional_parameters)
        return response(response_data)
     return HttpResponse(status=400)