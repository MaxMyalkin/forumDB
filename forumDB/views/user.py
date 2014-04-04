from forumDB.functions.common import make_required, make_optional, response_error, response_ok
from forumDB.functions.post.getters import get_user_post_list
from forumDB.functions.user.user_functions import *

__author__ = 'maxim'


def create(request):
    if request.method == 'POST':
        try:
            optional_parameters = make_optional("POST", request, ['isAnonymous', 'name', 'username', 'about'])
            if optional_parameters['isAnonymous'] == True:
                required_params = make_required("POST", request, ['email', ])
            else:
                required_params = make_required("POST", request, ['email','name', 'username', 'about' ])
            response_data = create_user(required_params, optional_parameters)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    else:
        return response_error('incorrect type of request')


def follow(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['follower', 'followee'])
            response_data = save_follow(required_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def unfollow(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['follower', 'followee'])
            response_data = remove_follow(required_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def details(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['user'])
            response_data = get_user_details(required_params['user'])
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def list_followers(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['user'])
            optional_parameters = make_optional("GET", request, ['limit', 'since_id', 'order'])
            response_data = get_list_followers(required_params, optional_parameters)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def list_following(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET" , request, ['user'])
            optional_parameters = make_optional("GET", request, ['limit', 'since_id', 'order'])
            response_data = get_list_following(required_params, optional_parameters)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def update(request):
    if request.method == 'POST':
        try:
            required_params = make_required("POST", request, ['user', 'name', 'about'])
            response_data = update_user(required_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    return response_error('incorrect type of request')


def list_posts(request):
    if request.method == 'GET':
        try:
            required_params = make_required("GET", request, ['user'])
            optional_params = make_optional("GET", request, ['since', 'limit', 'order'])
            response_data = get_user_post_list(required_params,optional_params)
            return response_ok(response_data)
        except Exception as exception:
            return response_error(exception.message)
    else:
        return response_error('incorrect type of request')