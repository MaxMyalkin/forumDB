import json
from django.http import HttpResponse

__author__ = 'maxim'

def response(response_data):
    if response_data is not None:
            return HttpResponse(json.dumps({'code': 0, 'response': response_data}), content_type='application/json')
    else:
        return HttpResponse(status=400)