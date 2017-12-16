from django.conf.urls import include, url

from proposal.views import *

app_name = 'proposal'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^edit/', edit, name='edit'),
    url(r'^bimbingan/$', bimbingan, name='bimbingan'),
    url(r'^bimbingan/tambah/', tambah, name='tambah'),
    url(r'^sidang', sidang, name='sidang')
]
