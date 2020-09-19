from django.urls import path
from .views import *

app_name = 'api_v1'

urlpatterns = [
    path('contact_us', contact_us, name='contact_us')
]