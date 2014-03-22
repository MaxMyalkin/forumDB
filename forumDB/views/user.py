import json
from django.http import HttpResponse
from forumDB.functions.database import *
from forumDB.functions.user_functions import *
__author__ = 'maxim'


def create(request):
    if(request.method == 'POST'):
        request_data = json.loads(request.body)
        email = request_data['email']
        name = request_data['name']
        username = request_data['username']
        about = request_data['about']
        try:
            anonymous = int(request_data['isAnonymous'])
        except KeyError:
            anonymous = 0
        response_data = saveUser(email , name , username , about , anonymous)
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    else:
        return HttpResponse(status=400)



def follow(request):
     if(request.method == 'POST'):
        request_data = json.loads(request.body)
        follower = request_data['follower']
        followee = request_data['followee']
        response_data = saveFollow(follower, followee)
        if(response_data != None):
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
     return HttpResponse(status=400)



def unfollow(request):
     if(request.method == 'POST'):
        request_data = json.loads(request.body)
        follower = request_data['follower']
        followee = request_data['followee']
        response_data = removeFollow(follower, followee)
        if(response_data != None):
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
     return HttpResponse(status=400)

def details(request):
    if(request.method == 'POST'):
        #email = request.GET.get('email')
        request_data = json.loads(request.body)
        email = request_data['user']
        response_data = getDetails(email)
        if(response_data != None):
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    return HttpResponse(status=400)

def update(request):
    if(request.method == 'POST'):
        request_data = json.loads(request.body)
        email = request_data['email']
        name = request_data['name']
        about = request_data['about']
        response_data = updateUser(email , name , about)
        return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    else:
        return HttpResponse(status=400)