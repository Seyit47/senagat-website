from django.http import HttpResponse

BAD_REQUEST = HttpResponse(
    status = 400,
    content='Bad Request'
)