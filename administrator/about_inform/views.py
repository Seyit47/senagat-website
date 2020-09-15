from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='administrator:login')
def about_inform(request):
    return render(request, 'administrator/about_inform.html', 
    {'page':'about_inform'})