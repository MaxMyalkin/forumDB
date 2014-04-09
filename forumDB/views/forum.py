from forumDB.functions.common import make_required, make_optional, response_error, response_ok
from forumDB.functions.forum.forum_functions import create_forum, get_forum_details
from forumDB.functions.forum.getters import get_list_threads
from forumDB.functions.post.getters import get_forum_post_list
from forumDB.functions.user.getters import get_forum_user_list

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['name', 'short_name', 'user'])
            response_data = create_forum(required_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def details(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['forum'])
            optional = make_optional("GET" , request , ['related'])
            response_data = get_forum_details(required_params['forum'], optional['related'])
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def list_threads(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['forum'])
            optional_parameters = make_optional("GET", request, ['since', 'limit', 'order', 'related'])
            response_data = get_list_threads('forum', required_params['forum'],optional_parameters['related'], optional_parameters)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def list_posts(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['forum'])
            optional_params = make_optional("GET", request, ['since', 'limit', 'order', 'related'])
            response_data = get_forum_post_list(required_params, optional_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def list_users(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['forum'])
            optional_params = make_optional("GET", request, ['since_id', 'limit', 'order'])
            response_data = get_forum_user_list(required_params, optional_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')