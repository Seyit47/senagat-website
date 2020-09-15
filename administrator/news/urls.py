from django.urls import path
from .views import *

urlpatterns = [
    path('', news, name='news'),
    path('new/', news_create, name='news_create'),
    path('edit/<int:pk>', news_edit, name='news_edit')
]