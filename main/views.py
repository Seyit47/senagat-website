from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .helpers import get_pagination, get_day_time
from .documents import NewsDocument, TenderDocument
from django.core.mail import send_mail
from api_v1.tasks import *
from modules.constants import *
from django import forms
from django.conf import settings
import json
import urllib
import logging
from .responses import BAD_REQUEST
from modules.exceptions import ExceptionInvalidForm
from math import floor
from random import random
from captcha.image import ImageCaptcha




logger = logging.getLogger(__name__)

def home(request):
    site_settings = Settings.objects.all()
    news = News.objects.all().order_by('-created_date')[:8]
    magazines = Magazine.objects.filter().order_by('-created_date')
    factories = Factory.objects.all().order_by('created_date')
    tender = Tender.objects.all().order_by('-created_date')[:4]
    day_time = get_day_time(timezone.localtime())

    q = request.GET.get('q')

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    q = request.GET.get('q')

    if q:
        tenders = TenderDocument.search().query("match", title=q)
    else:
        tenders = ''

     
    return render(request, 'main/home.html',
    {
        'news':news,
        'site_settings':site_settings,
        'factories':factories,
        'tender':tender,
        'magazines':magazines,
        'day_time':day_time,
        'page':'home',
        'item':item,
        'tenders':tenders
    })

def news(request):
    site_settings = Settings.objects.all()
    LIMIT = 10
    page  = request.GET.get('page', 1)
    count      = News.objects.filter(show = True).count()
    pagination = get_pagination(page, count, LIMIT)
    
    offset = (pagination['page'] - 1) * LIMIT
    news = News.objects.filter(show = True).order_by('-created_date')[offset:offset + LIMIT]

    q = request.GET.get('q')

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    return render(request, 'main/news.html', 
    {
        'news':news,
        'pagination':pagination,
        'page':'news',
        'site_settings':site_settings,
        'item':item,
    })

def news_detail(request, pk):
    site_settings = Settings.objects.all()
    news = News.objects.filter(pk = pk)

    q = request.GET.get('q')

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    try:
        prv = news[0].get_previous_by_created_date()
    except:
        prv = False
    try:
        nxt = news[0].get_next_by_created_date()
    except:
        nxt = False
    return render(request, 'main/news_detail.html', 
    {'news': news[0],
    'next':nxt,
    'prev':prv,
    'site_settings':site_settings,
    'page':'news',
    'item':item
    })

def about_us(request):
    site_settings = Settings.objects.all()
    gallery = Gallery.objects.all().order_by('date')
    day_time = get_day_time(timezone.localtime())

    q = request.GET.get('q')

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    return render(request, 'main/about_us.html', 
    {'page':'about_us',
    'gallery':gallery,
    'site_settings':site_settings,
    'day_time':day_time,
    'item':item
    })

def factory_detail(request, pk):
    site_settings = Settings.objects.all()
    factory = Factory.objects.filter(pk = pk)

    q = request.GET.get('q')

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    return render(request, 'main/factory_detail.html', 
    {'factory':factory[0],
    'site_settings':site_settings,
    'background_video': factory[0].video,
    'item':item
    })

def tender(request):
    site_settings = Settings.objects.all()
    LIMIT = 6
    page = request.GET.get('page', 1)
    count = News.objects.filter(show=True).count()
    pagination = get_pagination(page, count, LIMIT)
    
    offset = (pagination['page'] - 1) * LIMIT
    tender = Tender.objects.filter(show = True).order_by('-created_date')[offset:offset + LIMIT]

    q = request.GET.get('q')

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    return render(request, 'main/tender.html', 
    {'tender':tender,
    'pagination':pagination,
    'page':'tender',
    'site_settings':site_settings,
    'item':item
    })

def tender_detail(request, pk):
    tender = Tender.objects.filter(pk = pk)
    site_settings = Settings.objects.all()

    q = request.GET.get('q')

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    return render(request, 'main/tender_detail.html', 
    {
        'tender':tender[0],
        'page':'tender',
        'site_settings':site_settings,
        'item':item
    })

def document(request):
    site_settings = Settings.objects.all()

    q = request.GET.get('q')

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    return render(request, 'main/document.html', 
    {
        'site_settings':site_settings,
        'page':'document',
        'item':item
    })


def contact_us(request):
    assocations = AssocationContacts.objects.all().order_by('-create_ts')
    site_settings = Settings.objects.all()

    q = request.GET.get('q')

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    

    no = '1234567890QWERTYUIPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    x = no[floor(random() * len(no))]
    for i in range(1,6):
        x = x + no[floor(random() * len(no))]

    image = ImageCaptcha()
    data = image.generate_image(x)
    images = image.write(x, x + '.jpg')


    if request.method == 'POST':
        form = {}
        form['message_name'] = request.POST.get('message-name', '')
        form['message_email'] = request.POST.get('message-email', '')
        form['message'] = request.POST.get('message', '')

        
        try:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response':recaptcha_response
            }

            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            
            if result['success']:
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
                return render(request, 'main/contact_us.html', 
                    {'message_name':form['message_name'],
                    'assocations':assocations,
                    'site_settings':site_settings,
                    'page':'contact_us',
                    'item':item,
                })
            else:
                logger.exception('func: contact_us; msg: Catched exception invalid form ')
                return BAD_REQUEST
        except ExceptionInvalidForm:
            logger.exception('func: contact_us; msg: Catched exception invalid form ')
            return BAD_REQUEST
    
    return render(request, 'main/contact_us.html', 
    {
        'assocations':assocations,
        'site_settings':site_settings,
        'page':'contact_us',
        'item':item,
        'captcha':images
    })

def search(request):
    q = request.GET.get('q')
    site_settings = Settings.objects.all()

    if q:
        item = NewsDocument.search().query("match", title=q)
    else:
        item = ''

    q = request.GET.get('q')

    if q:
        tenders = TenderDocument.search().query("match", title=q)
    else:
        tenders = ''

    return render(request, 'main/search.html', 
    {
        'item':item,
        'tenders':tenders,
        'site_settings':site_settings
    })

def order(request):
    site_settings = Settings.objects.all()
    

    if request.method == 'POST':
        form = {}
        form['product'] = request.POST.get('product', '')
        form['who_is'] = request.POST.get('who_is', '')
        form['fullname'] = request.POST.get('fullname', '')
        form['organization'] = request.POST.get('organization', '')
        form['phone'] = request.POST.get('phone', '')
        form['email'] = request.POST.get('email', '')
        form['capacity'] = request.POST.get('capacity', '')
        form['shipping_method'] = request.POST.get('shipping_method', '')

        form['letter'] = request.FILES.get('letter', '')
        form['contract'] = request.FILES.get('contract', '')
        form['certificate'] = request.FILES.get('certificate', '')
        form['wes_certificate'] = request.FILES.get('wes_certificate', '')
        form['state_license'] = request.FILES.get('state_license', '')
        form['egrpo'] = request.FILES.get('egrpo', '')
        form['banking_details'] = request.FILES.get('banking_details', '')

        try:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response':recaptcha_response
            }

            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                orders = Order.objects.create(
                    product = form['product'],
                    phone = form['phone'],
                    fullname = form['fullname'],
                    who_is = form['who_is'],
                    organization = form['organization'],
                    email = form['email'],
                    capacity = form['capacity'],
                    shipping_method = form['shipping_method'],
                    letter = form['letter'],
                    contract = form['contract'],
                    certificate = form['certificate'],
                    wes_certificate = form['wes_certificate'],
                    state_license = form['state_license'],
                    egrpo = form['egrpo'],
                    banking_details = form['banking_details'] 
                )
            

                send_mail(
                    form['fullname'],
                    form['product'],
                    form['email'],
                    ['seyitbu1111@gmail.com']
                )
            else:
                logger.exception('func: contact_us; msg: Catched exception invalid form ')
                return BAD_REQUEST

        except ExceptionInvalidForm:
            logger.exception('func: contact_us; msg: Catched exception invalid form ')
            return BAD_REQUEST


    return render(request, 'main/order.html', 
    {
        'site_settings':site_settings,
        'page':'order',
        'products':ONLINE_ORDER_PRODUCTS,
        'shipping_methods':ONLINE_ORDER_SHIPPING_METHODS,
        'who_is':ONLINE_ORDER_WHO_IS
    })


