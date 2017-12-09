from django.conf.urls import include, url
from skripsi.views import *

urlpatterns = [
    url(r'^$',dexskripsi,name='dexskripsi'),
    url(r'^bimbingan/',bimbingan,name='bimbingan'),
    url(r'^sidang',sidang,name='sidang')
]
