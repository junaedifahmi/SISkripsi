from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from proposal.views import *

app_name = 'proposal'

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
    url(r'^edit/', edit, name='edit'),
    url(r'^bimbingan/$', login_required(bimbingan), name='bimbingan'),
    url(r'^bimbingan/tambah/', tambah, name='tambah'),
    url(r'^sidang', login_required(sidang), name='sidang')
]
