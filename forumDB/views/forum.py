from django.http import HttpResponse
from forumDB.functions.common import response, make_required, make_optional
from forumDB.functions.forum.forum_functions import create_forum, get_forum_details
from forumDB.functions.forum.getters import get_listThreads
from forumDB.functions.post.getters import get_forum_post_list
from forumDB.functions.user.getters import get_forum_user_list

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        required_params = make_required("POST", request, ['name', 'short_name', 'user'])
        if required_params is None:
            return HttpResponse(status=400)
        response_data = create_forum(required_params)
        return response(response_data)
    return HttpResponse(status=400)


def details(request):
    if request.method == 'GET':
        required_params = make_required("GET", request, ['forum'])
        if required_params is None:
            return HttpResponse(status=400)
        try:
            related = request.GET.get('related')
        except KeyError:
            related = []
        response_data = get_forum_details(required_params['forum'], related)
        return response(response_data)
    return HttpResponse(status=400)


def listThreads(request):
    if request.method == 'GET':
        required_params = make_required("GET", request, ['forum'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_parameters = make_optional("GET", request, ['since', 'limit', 'order', 'related'])
        response_data = get_listThreads('forum', required_params['forum'],optional_parameters['related'], optional_parameters)
        return response(response_data)
    return HttpResponse(status=400)


def list_posts(request):
    if request.method == 'GET':
        required_params = make_required("GET", request, ['forum'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_params = make_optional("GET", request, ['since', 'limit', 'order', 'related'])
        response_data = get_forum_post_list(required_params,optional_params)
        return response(response_data)
    else:
        return HttpResponse(status=400)


def list_users(request):
    if request.method == 'GET':
        required_params = make_required("GET", request, ['forum'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_params = make_optional("GET", request, ['since_id', 'limit', 'order'])
        response_data = get_forum_user_list(required_params,optional_params)
        return response(response_data)
    else:
        return HttpResponse(status=400)