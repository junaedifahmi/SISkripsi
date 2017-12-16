from django.shortcuts import render, redirect, get_object_or_404
from base.models import User
import string

# Create your views here.


def dex(request):
    """
    Ini untuk menampilkan landing page

    :param request:
    :return:
    """
    return render(request, 'dex.html')


def home(request):
    """
    Ini untuk ke beranda

    :param request:
    :return:
    """

    return render(request, 'home.html')


def login(request):
    """
    ini untuk proses login
    :param request:
    :return:
    """

    redir = "base:dex"
    if request.method == 'POST':
        mail = request.POST.get('email')
        pwd = request.POST.get('pw')
        a = User.objects.get(pk=mail)
        if a.pw == pwd:
            request.session['user'] = id(a)
            print(request.session['user'])
            redir = "base:home"

    else:
        redir = "base:dex"

    return redirect(redir)
