from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http   import require_http_methods
from django.contrib.auth import authenticate, login, logout
import logging


logger = logging.getLogger(__name__)

@login_required(login_url='administrator:login')
def home(request):
    return redirect('administrator:news')

@require_http_methods(['GET', 'POST'])
def log_in(request):
    nxt = request.GET.get('next', 'administrator:home')
    if request.user.is_authenticated:
        return redirect(nxt)

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username = username, password = password)
        if user is None:
            raise Http404

        login(request, user)
        return redirect(nxt)
    return render(request,'administrator/login.html')


def log_out(request):
    logger.info('User with username=<%s> logged out' % request.user)
    logout(request)
    return redirect('administrator:login')
