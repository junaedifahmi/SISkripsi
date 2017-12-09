from django.conf.urls import include, url
from proposal.views import *

urlpatterns = [
    url(r'^$',dexprop,name='dexprop'),
    url(r'^bimbingan/',bimbingan,name='bimbingan'),
    url(r'^sidang',sidang,name='sidang')
]
