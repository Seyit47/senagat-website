from django.urls import path, include
from .views import *

app_name = 'administrator'
urlpatterns = [
    path('', home, name = 'home'),
    path('login/',  log_in,  name = 'login'),
    path('logout/', log_out, name = 'logout'),
    
    path('news/',        include('administrator.news.urls')),
    path('about_inform', include('administrator.about_inform.urls'))
]