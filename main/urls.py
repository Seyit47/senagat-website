from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', home, name='home'),
    path('news/', news, name='news'),
    path('news/<int:pk>', news_detail, name='news_detail'),
    path('about_us/', about_us, name='about_us'),
    path('factory/<int:pk>', factory_detail, name='factory_detail'),
    path('tender/', tender, name='tender'),
    path('tender/<int:pk>', tender_detail, name='tender_detail'),
    path('documents/', document, name='document'),
    path('contact_us/', contact_us, name='contact_us'),
    path('search/', search, name='search'),
    path('online-order/', order, name='order')
]