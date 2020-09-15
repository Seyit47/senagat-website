from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .helpers import get_pagination, get_day_time
from .forms import *
from .documents import NewsDocument, TenderDocument
from api_v1.tasks import send_email_task


def home(request):
    site_settings = Settings.objects.all()
    news = News.objects.all().order_by('-created_date')[:8]
    magazines = Magazine.objects.filter().order_by('-created_date')
    factories = Factory.objects.all().order_by('created_date')
    tender = Tender.objects.all().order_by('-created_date')[:4]
    day_time = get_day_time(timezone.localtime())
    send_email_task()

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

    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            message = forms.save(commit=False)
            message.save()
            return redirect('main:contact_us')
    else:
        forms = ContactForm()

    return render(request, 'main/contact_us.html', 
    {
        'assocations':assocations,
        'site_settings':site_settings,
        'page':'contact_us',
        'forms':forms,
        'item':item
    })

def search(request):
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

    return render(request, 'main/search.html', 
    {
        'item':item,
        'tenders':tenders,
    })