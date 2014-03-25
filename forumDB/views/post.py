import json
from django.http import HttpResponse
from forumDB.functions.common import make_required, response, make_optional
from forumDB.functions.post.post_functions import save_post

__author__ = 'maxim'

def create(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        required_params =  make_required(request_data,['date','thread','message','user' , 'forum'])
        if required_params is None:
            return HttpResponse(status=400)
        optional_parameters = make_optional(request_data , ['parent' , 'isApproved' , 'isHighlighted' , 'isEdited' , 'isSpam' , 'isDeleted'])
        response_data = save_post(required_params , optional_parameters)
        return response(response_data)
    else:
        return HttpResponse(status=400)