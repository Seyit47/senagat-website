from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.conf                  import settings

from main.models import Contact_us, Order

@require_http_methods(['POST'])
def contact_us(request):
    form = {}
    form['message_name'] = request.POST.get['message-name']
    form['message_email'] = request.POST.get['message-email']
    form['message'] = request.POST.get['message']
    
    messages = Contact_us.objects.create(
        fullname = form['message_name'],
        email = form['message_email'],
        message = form['message'],
    )   

    send_mail(
        form['message_name'],
        form['message'],
        form['message_email'],
        ['seyitbu1111@gmail.com']
    )
    