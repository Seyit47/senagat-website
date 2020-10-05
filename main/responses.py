from django.http import HttpResponse
import json

BAD_REQUEST = HttpResponse(
    status = 400,
    content='Bad Request'
)

INTERNAL_SERVER_ERROR = HttpResponse(
    status = 500,
    content = 'Internal Server error'
)

TOO_MANY_REQUESTS = HttpResponse(
    status = 429,
    content='Too many requests'
)

def get_response(content = ''):
    return HttpResponse(
        status = 200,
        content_type='application/json', 
        content = json.dumps(content)
    )

BOLLY_BLOK_SEN_JIGIM = HttpResponse(
    status = 516,
    content = 'Bolly blok sen jigim'
)