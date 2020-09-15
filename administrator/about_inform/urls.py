from django.urls import path
from .views import *

urlpatterns = [
    path('', about_inform, name='about_inform')
]